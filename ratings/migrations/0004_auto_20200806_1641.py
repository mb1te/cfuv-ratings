# Generated by Django 3.1 on 2020-08-06 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0003_abiturient_type_of_study'),
    ]

    operations = [
        migrations.CreateModel(
            name='FieldOfStudy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(default='', max_length=255)),
                ('name', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.RenameField(
            model_name='abiturient',
            old_name='field_of_study',
            new_name='field',
        ),
        migrations.RenameField(
            model_name='abiturient',
            old_name='form_of_study',
            new_name='form',
        ),
        migrations.RenameField(
            model_name='abiturient',
            old_name='type_of_study',
            new_name='type',
        ),
    ]
