# Generated by Django 3.0.6 on 2020-05-07 18:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20200315_0356'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sluglineuser',
            options={'ordering': ['date_joined']},
        ),
    ]
