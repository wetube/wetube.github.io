# encoding: utf8
from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20140329_1045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='blog_TimeDate',
            field=models.DateTimeField(default=datetime.datetime(2014, 3, 29, 10, 57, 55, 50267)),
        ),
    ]
