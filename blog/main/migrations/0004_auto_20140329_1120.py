# encoding: utf8
from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20140329_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='blog_TimeDate',
            field=models.DateTimeField(default=datetime.datetime(2014, 3, 29, 11, 20, 45, 479646), verbose_name='Date and Time Published'),
        ),
    ]
