# Generated by Django 3.0.3 on 2020-03-07 17:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0006_auto_20200307_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adlist',
            name='post_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 7, 17, 8, 36, 21989)),
        ),
    ]