# Generated by Django 2.0.2 on 2018-05-28 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20180525_1242'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='location',
            field=models.CharField(default='Warszawa', max_length=512),
            preserve_default=False,
        ),
    ]
