# Generated by Django 4.2.2 on 2023-09-13 10:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zohoapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loan',
            name='comment',
        ),
    ]
