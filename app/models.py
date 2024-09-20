from django.db import models
import uuid

# Create your models here.
class School(models.Model):
    school_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Class(models.Model):
    class_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class AssessmentAreas(models.Model):
    assessment_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Student(models.Model):
    student_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    student_class = models.ForeignKey(Class, on_delete=models.CASCADE)
    year_level = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Answers(models.Model):
    answer_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    answers = models.TextField()

    def __str__(self):
        return self.answers

class Awards(models.Model):
    award_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Subject(models.Model):
    subject_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    subject = models.CharField(max_length=100)
    subject_score = models.FloatField()
    assessment_area = models.ForeignKey(AssessmentAreas, on_delete=models.CASCADE)

    def __str__(self):
        return self.subject

class Summary(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    sydney_participant = models.IntegerField()
    sydney_percentile = models.FloatField()
    assessment_area = models.ForeignKey(AssessmentAreas, on_delete=models.CASCADE)
    award = models.ForeignKey(Awards, on_delete=models.SET_NULL, null=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    correct_answer_percentage_per_class = models.FloatField()
    correct_answer = models.CharField(max_length=100)
    year_level_name = models.CharField(max_length=50)
    student_score = models.FloatField()
    average_score = models.FloatField()
    school_percentile = models.FloatField()
    sydney_correct_count_percentage = models.FloatField()
    participant = models.BooleanField()
    total_area_assessed_score = models.FloatField()

    def __str__(self):
        return f"Summary for {self.student} - {self.subject}"
