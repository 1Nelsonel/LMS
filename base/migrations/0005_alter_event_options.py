# Generated by Django 4.0.5 on 2022-08-09 20:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_event_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['event_date', 'start_time']},
        ),
    ]