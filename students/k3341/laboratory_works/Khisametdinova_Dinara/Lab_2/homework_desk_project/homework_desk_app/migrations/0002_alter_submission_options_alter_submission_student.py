# Generated by Django 5.1.2 on 2024-10-29 11:25

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homework_desk_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='submission',
            options={'permissions': [('can_grade_submissions', 'Can grade submissions')]},
        ),
        migrations.AlterField(
            model_name='submission',
            name='student',
            field=models.ForeignKey(limit_choices_to={'role': 'student'}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
