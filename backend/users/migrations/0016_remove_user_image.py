# Generated by Django 2.2.28 on 2023-05-25 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_remove_callcenter_patientid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='image',
        ),
    ]