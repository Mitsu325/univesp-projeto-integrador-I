# Generated by Django 4.2.11 on 2024-04-09 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumes', '0005_gender_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='educationlevel',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
