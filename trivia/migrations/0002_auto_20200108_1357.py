# Generated by Django 3.0 on 2020-01-08 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trivia', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='points',
        ),
        migrations.AddField(
            model_name='question',
            name='points',
            field=models.IntegerField(default=10, help_text='number of points given for getting the correct answer to this question'),
        ),
    ]
