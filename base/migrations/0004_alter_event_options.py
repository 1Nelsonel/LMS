# Generated by Django 4.0.5 on 2022-08-09 20:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_event'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['-event_date', '-start_time']},
        ),
    ]
