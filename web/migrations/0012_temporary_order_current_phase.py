# Generated by Django 5.0.2 on 2024-02-27 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0011_alter_temporary_order_order_create_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='temporary_order',
            name='current_phase',
            field=models.IntegerField(default=1, verbose_name='当前期数'),
            preserve_default=False,
        ),
    ]
