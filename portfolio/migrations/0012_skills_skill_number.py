# Generated by Django 3.2.13 on 2022-06-12 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0011_skills'),
    ]

    operations = [
        migrations.AddField(
            model_name='skills',
            name='skill_number',
            field=models.IntegerField(default=0),
        ),
    ]
