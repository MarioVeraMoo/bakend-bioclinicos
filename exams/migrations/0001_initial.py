# Generated by Django 5.1.3 on 2024-11-27 23:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('titleExam', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('discount', models.IntegerField()),
                ('description', models.TextField(blank=True, null=True)),
                ('indications', models.TextField(blank=True, null=True)),
                ('miniature', models.ImageField(blank=True, null=True, upload_to='categories/images/')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='categories.category')),
            ],
        ),
    ]