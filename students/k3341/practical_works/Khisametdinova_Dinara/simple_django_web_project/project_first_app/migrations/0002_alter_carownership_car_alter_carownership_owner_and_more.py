# Generated by Django 5.1.2 on 2024-11-17 19:43

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_first_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carownership',
            name='car',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ownerships', to='project_first_app.car'),
        ),
        migrations.AlterField(
            model_name='carownership',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ownerships', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='driverlicense',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='licenses', to=settings.AUTH_USER_MODEL),
        ),
    ]
