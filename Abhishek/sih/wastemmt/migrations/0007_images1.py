# Generated by Django 3.0.2 on 2020-01-20 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wastemmt', '0006_auto_20200120_0723'),
    ]

    operations = [
        migrations.CreateModel(
            name='images1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('garbageimage1', models.ImageField(default='', upload_to='wastemmt1/images')),
            ],
        ),
    ]
