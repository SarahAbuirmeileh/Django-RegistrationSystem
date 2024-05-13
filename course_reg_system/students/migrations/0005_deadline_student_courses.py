# Generated by Django 5.0.4 on 2024-05-13 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
        ('students', '0004_delete_deadline_remove_student_courses'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deadline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=255)),
                ('due_date', models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='courses',
            field=models.ManyToManyField(related_name='students', through='students.StudentRegistration', to='courses.course'),
        ),
    ]
