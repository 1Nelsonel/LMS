# Generated by Django 4.0.5 on 2022-08-10 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_remove_curriculum_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='curriculum',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
