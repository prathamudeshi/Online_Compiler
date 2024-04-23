# Generated by Django 4.2.5 on 2024-04-22 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pycompiler', '0006_code_qs_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='code',
            name='id',
        ),
        migrations.AddField(
            model_name='code',
            name='code_id',
            field=models.IntegerField(default=1, primary_key=True, serialize=False, unique=True),
        ),
    ]
