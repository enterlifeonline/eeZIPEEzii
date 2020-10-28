# Generated by Django 3.1.1 on 2020-09-12 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job', models.IntegerField()),
                ('user', models.IntegerField()),
                ('url', models.URLField()),
                ('status', models.TextField()),
                ('description', models.TextField(blank=True)),
            ],
        ),
    ]
