# Generated by Django 2.2 on 2019-05-15 08:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('friends', '0004_auto_20190515_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_created',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
