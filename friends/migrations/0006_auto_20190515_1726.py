# Generated by Django 2.2 on 2019-05-15 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('friends', '0005_auto_20190515_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]