# Generated by Django 3.1.4 on 2021-03-08 19:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20210307_2041'),
        ('blogs', '0007_auto_20210307_2321'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(choices=[('English', 'English'), ('Nepali', 'Nepali'), ('Hindi', 'Hindi'), ('Korean', 'Korean'), ('Japanese', 'Japanese')], max_length=100)),
                ('jobseeker_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.jobseeker')),
            ],
        ),
        migrations.RenameModel(
            old_name='Jobseeker_education',
            new_name='Education',
        ),
        migrations.RenameModel(
            old_name='Jobseeker_employment',
            new_name='Employment',
        ),
        migrations.RenameModel(
            old_name='Jobseeker_skill',
            new_name='Skill',
        ),
        migrations.DeleteModel(
            name='Jobseeker_language',
        ),
    ]
