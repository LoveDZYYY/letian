# Generated by Django 5.0.2 on 2024-02-25 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_open_shengxiao'),
    ]

    operations = [
        migrations.AddField(
            model_name='open_shengxiao',
            name='current_phase',
            field=models.IntegerField(default=1, verbose_name='目前阶段'),
            preserve_default=False,
        ),
    ]