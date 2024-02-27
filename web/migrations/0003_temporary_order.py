# Generated by Django 5.0.2 on 2024-02-25 10:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_alter_user_mobile_alter_user_money'),
    ]

    operations = [
        migrations.CreateModel(
            name='temporary_order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_buy_goods', models.CharField(max_length=200, verbose_name='用户购买的赌具')),
                ('stay_pay_money', models.IntegerField(verbose_name='待支付余额')),
                ('order_create_time', models.DateTimeField(auto_now_add=True, verbose_name='订单创建时间')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.user')),
            ],
        ),
    ]