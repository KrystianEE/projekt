# Generated by Django 2.0.2 on 2018-05-29 08:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_auto_20180528_1158'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='owner',
            new_name='user',
        ),
    ]
