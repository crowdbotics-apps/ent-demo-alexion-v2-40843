# Generated by Django 2.2.28 on 2023-05-25 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20230525_1639'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='generalNotes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.URLField(blank=True, null=True),
        ),
    ]
