# Generated by Django 3.1 on 2020-08-06 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='abiturient',
            name='form_of_study',
            field=models.CharField(default='', max_length=255),
        ),
    ]
