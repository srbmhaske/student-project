# Generated by Django 3.2.8 on 2021-10-08 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_alter_student_student_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_no',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
    ]
