# Generated by Django 2.0.6 on 2018-06-26 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20180622_1446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(error_messages={'unique': 'A user with that phone number already exists.'}, max_length=12, unique=True, verbose_name='phone number'),
        ),
    ]
