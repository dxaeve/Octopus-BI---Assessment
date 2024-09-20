import csv
from django.core.management.base import BaseCommand
from app.models import School, Class, Student, Subject, AssessmentAreas, Answers, Awards, Summary
from uuid import uuid4

class Command(BaseCommand):
    help = 'Load dataset into the database from a CSV file with an optional limit on rows'

    def add_arguments(self, parser):
        parser.add_argument('path', type=str, help='The file path to the CSV file')

        parser.add_argument('--limit', type=int, help='Limit the number of rows to process from the CSV file')

    def handle(self, *args, **kwargs):
        file_path = kwargs['path']
        limit = kwargs.get('limit')

        try:
            with open(file_path, 'r') as csvfile:
                reader = csv.DictReader(csvfile)

                for idx, row in enumerate(reader):
                    if limit is not None and idx >= limit:
                        break

                    school, created = School.objects.get_or_create(
                        name=row['school_name']
                    )

                    student_class, created = Class.objects.get_or_create(
                        name=row['Class']
                    )

                    assessment_area, created = AssessmentAreas.objects.get_or_create(
                        name=row['Assessment Areas']
                    )

                    subject, created = Subject.objects.get_or_create(
                        subject=row['Subject'],
                        subject_score=row['student_score'],
                        assessment_area=assessment_area
                    )

                    award, created = Awards.objects.get_or_create(
                        name=row['award']
                    )

                    student, created = Student.objects.get_or_create(
                        first_name=row['First Name'],
                        last_name=row['Last Name'],
                        school=school,
                        student_class=student_class,
                        year_level=row['Year Level']
                    )

                    answer, created = Answers.objects.get_or_create(
                        answers=row['Answers']
                    )

                    Summary.objects.create(
                        school=school,
                        sydney_participant=int(row['sydney_participants']),
                        sydney_percentile=float(row['sydney_percentile']),
                        assessment_area=assessment_area,
                        award=award,
                        student=student,
                        subject=subject,
                        correct_answer_percentage_per_class=float(row['correct_answer_percentage_per_class']),
                        correct_answer=row['Correct Answers'],
                        year_level_name=row['Year Level'],
                        student_score=float(row['student_score']),
                        average_score=float(row['average_score']),
                        school_percentile=float(row['school_percentile']),
                        sydney_correct_count_percentage=float(row['sydney_correct_count_percentage']),
                        participant=bool(int(row['participant'])),
                        total_area_assessed_score=float(row['total_area_assessed_score']),
                    )

            self.stdout.write(self.style.SUCCESS(f'Data successfully loaded from {file_path} (limited to {limit} rows)!' if limit else f'Data successfully loaded from {file_path}!'))

        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f"File at {file_path} not found! Please provide a valid path."))
