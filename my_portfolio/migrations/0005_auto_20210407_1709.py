# Generated by Django 3.1.7 on 2021-04-07 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_portfolio', '0004_auto_20210406_1503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='views',
            field=models.IntegerField(default=0, verbose_name='Количество просмотров'),
        ),
    ]
