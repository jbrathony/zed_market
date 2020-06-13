# Generated by Django 3.0.3 on 2020-03-09 04:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0008_auto_20200308_1325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adlist',
            name='ad_rating',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='adlist',
            name='post_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]