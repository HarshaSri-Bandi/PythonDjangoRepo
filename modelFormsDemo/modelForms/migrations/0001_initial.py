# Generated by Django 5.1.2 on 2024-11-05 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startDate', models.DateField()),
                ('endDate', models.DateField()),
                ('name', models.CharField(max_length=30)),
                ('assignedTo', models.CharField(max_length=20)),
                ('priority', models.IntegerField()),
            ],
        ),
    ]
