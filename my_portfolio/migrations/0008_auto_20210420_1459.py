# Generated by Django 3.1 on 2021-04-20 07:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_portfolio', '0007_auto_20210414_1352'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='skills',
            options={'ordering': ['ordering'], 'verbose_name': 'Навык', 'verbose_name_plural': 'Навыки'},
        ),
    ]
