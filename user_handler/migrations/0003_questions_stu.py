# Generated by Django 4.2.5 on 2024-04-20 18:44

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_handler', '0002_questions_testcase_student_qs_solved'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='stu',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
