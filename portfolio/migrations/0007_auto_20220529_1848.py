# Generated by Django 3.2.13 on 2022-05-29 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_auto_20220529_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='name_of_projects',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='project',
            name='participants_in_projects',
            field=models.ManyToManyField(to='portfolio.Person'),
        ),
    ]