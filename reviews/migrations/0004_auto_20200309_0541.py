# Generated by Django 3.0.3 on 2020-03-09 05:41

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_auto_20200309_0440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='post_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 9, 5, 41, 51, 926302, tzinfo=utc)),
        ),
    ]