# Generated by Django 5.0.3 on 2024-04-08 20:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_rename_schedule_id_course_schedule_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='prerequisites',
        ),
        migrations.RemoveField(
            model_name='course',
            name='schedule',
        ),
        migrations.RemoveField(
            model_name='studentregistration',
            name='course',
        ),
        migrations.RemoveField(
            model_name='studentregistration',
            name='student',
        ),
        migrations.DeleteModel(
            name='CourseSchedule',
        ),
        migrations.DeleteModel(
            name='Course',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.DeleteModel(
            name='StudentRegistration',
        ),
    ]
