# Generated by Django 4.2.7 on 2023-12-07 06:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Teachingapp', '0005_alter_event_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='tags',
        ),
    ]
