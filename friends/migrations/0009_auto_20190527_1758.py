# Generated by Django 2.2 on 2019-05-27 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('friends', '0008_auto_20190527_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]