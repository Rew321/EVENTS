# Generated by Django 4.2.7 on 2023-12-07 13:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Teachingapp', '0006_remove_event_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='starting_time',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]