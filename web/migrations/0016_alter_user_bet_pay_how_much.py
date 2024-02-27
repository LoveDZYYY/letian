# Generated by Django 5.0.2 on 2024-02-27 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0015_user_bet_pay_how_much'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_bet',
            name='pay_how_much',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=30, verbose_name='应付用户多少钱'),
        ),
    ]
