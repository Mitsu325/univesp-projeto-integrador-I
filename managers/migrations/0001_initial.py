# Generated by Django 4.2.11 on 2024-03-31 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=80, unique=True)),
                ('password', models.CharField(max_length=50)),
                ('user_type', models.CharField(choices=[('recruitment_manager', 'Recruitment Manager'), ('department_manager', 'Department Manager'), ('team_lead', 'Team Lead')], default='recruitment_manager', max_length=50)),
            ],
        ),
    ]
