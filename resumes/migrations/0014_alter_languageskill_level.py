# Generated by Django 4.2.12 on 2024-05-09 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumes', '0013_alter_education_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='languageskill',
            name='level',
            field=models.CharField(choices=[('basic', 'Básico'), ('intermediate', 'Intermediário'), ('advanced', 'Avançado')], max_length=50),
        ),
    ]