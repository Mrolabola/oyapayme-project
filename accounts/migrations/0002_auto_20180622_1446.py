# Generated by Django 2.0.6 on 2018-06-22 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='admin',
            options={'verbose_name': 'admin', 'verbose_name_plural': 'admins'},
        ),
        migrations.AlterModelOptions(
            name='agent',
            options={'verbose_name': 'agent', 'verbose_name_plural': 'agents'},
        ),
    ]