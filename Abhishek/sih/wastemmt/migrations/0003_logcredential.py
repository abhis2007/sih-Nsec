# Generated by Django 3.0.2 on 2020-01-19 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wastemmt', '0002_auto_20200120_0256'),
    ]

    operations = [
        migrations.CreateModel(
            name='logcredential',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usernames', models.CharField(max_length=50)),
                ('passwords', models.CharField(max_length=50)),
            ],
        ),
    ]