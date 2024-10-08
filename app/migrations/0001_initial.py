# Generated by Django 5.1.1 on 2024-09-20 17:18

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('answer_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('answers', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='AssessmentAreas',
            fields=[
                ('assessment_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Awards',
            fields=[
                ('award_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('class_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('school_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('year_level', models.CharField(max_length=50)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.school')),
                ('student_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.class')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('subject_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('subject', models.CharField(max_length=100)),
                ('subject_score', models.FloatField()),
                ('assessment_area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.assessmentareas')),
            ],
        ),
        migrations.CreateModel(
            name='Summary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sydney_participant', models.IntegerField()),
                ('sydney_percentile', models.FloatField()),
                ('correct_answer_percentage_per_class', models.FloatField()),
                ('correct_answer', models.CharField(max_length=100)),
                ('year_level_name', models.CharField(max_length=50)),
                ('student_score', models.FloatField()),
                ('average_score', models.FloatField()),
                ('school_percentile', models.FloatField()),
                ('sydney_correct_count_percentage', models.FloatField()),
                ('participant', models.BooleanField()),
                ('total_area_assessed_score', models.FloatField()),
                ('assessment_area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.assessmentareas')),
                ('award', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.awards')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.school')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.student')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.subject')),
            ],
        ),
    ]
