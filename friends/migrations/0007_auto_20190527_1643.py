# Generated by Django 2.2 on 2019-05-27 07:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('friends', '0006_auto_20190515_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='friend',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='friends.Friends'),
        ),
    ]