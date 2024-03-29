# Generated by Django 5.0.2 on 2024-02-24 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='mobile',
            field=models.CharField(max_length=32, unique=True, verbose_name='用户手机号'),
        ),
        migrations.AlterField(
            model_name='user',
            name='money',
            field=models.IntegerField(default=0, verbose_name='账户余额'),
        ),
    ]
