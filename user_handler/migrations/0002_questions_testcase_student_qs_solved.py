# Generated by Django 4.2.5 on 2024-04-17 10:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_handler', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('qs_id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('question', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TestCase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testcase_input', models.TextField()),
                ('expected_output', models.TextField()),
                ('qs_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_handler.questions')),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='qs_solved',
            field=models.ManyToManyField(blank=True, to='user_handler.questions'),
        ),
    ]
