# Generated by Django 4.2.11 on 2024-03-31 23:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('candidates', '0001_initial'),
        ('resumes', '0002_delete_resume'),
    ]

    operations = [
        migrations.CreateModel(
            name='AreaOfInterest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_birth', models.DateField()),
                ('telephone', models.CharField(max_length=15, null=True)),
                ('linkedin', models.CharField(max_length=50, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('area_of_interest', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='resumes.areaofinterest')),
                ('candidate', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='resume', to='candidates.candidate')),
            ],
        ),
    ]
