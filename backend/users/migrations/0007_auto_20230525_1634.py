# Generated by Django 2.2.28 on 2023-05-25 16:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_callcenter'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='generalNotes',
        ),
        migrations.RemoveField(
            model_name='user',
            name='recNextAppointment',
        ),
    ]