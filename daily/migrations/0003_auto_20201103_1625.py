# Generated by Django 3.1.2 on 2020-11-03 07:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('daily', '0002_auto_20201103_1114'),
    ]

    operations = [
        migrations.RenameField(
            model_name='daily',
            old_name='user',
            new_name='user_id',
        ),
    ]