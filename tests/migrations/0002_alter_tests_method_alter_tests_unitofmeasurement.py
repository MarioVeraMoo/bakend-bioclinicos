# Generated by Django 5.1.3 on 2024-12-05 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tests',
            name='method',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='tests',
            name='unitofmeasurement',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
