# Generated by Django 3.1.4 on 2021-03-07 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0004_jobseeker_education_jobseeker_employment_jobseeker_language_jobseeker_skill'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobseeker_profile',
            name='phone_number',
            field=models.PositiveBigIntegerField(blank=True, null=True),
        ),
    ]
