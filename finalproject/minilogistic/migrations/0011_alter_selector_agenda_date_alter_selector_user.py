# Generated by Django 4.1.4 on 2023-03-27 10:02

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('minilogistic', '0010_alter_selector_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='selector',
            name='agenda_date',
            field=models.DateField(default=datetime.datetime(2023, 3, 27, 10, 2, 28, 417300)),
        ),
        migrations.AlterField(
            model_name='selector',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='selectors', to=settings.AUTH_USER_MODEL),
        ),
    ]
