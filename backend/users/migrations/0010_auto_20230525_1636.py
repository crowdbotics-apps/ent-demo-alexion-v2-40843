# Generated by Django 2.2.28 on 2023-05-25 16:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20230525_1635'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='date',
        ),
        migrations.RemoveField(
            model_name='user',
            name='image',
        ),
    ]
