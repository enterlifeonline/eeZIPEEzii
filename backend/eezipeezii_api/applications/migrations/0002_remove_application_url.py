# Generated by Django 3.1.1 on 2020-09-12 00:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='url',
        ),
    ]
