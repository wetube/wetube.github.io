# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('blog_Poster', models.CharField(max_length=50)),
                ('blog_TimeDate', models.DateTimeField()),
                ('blog_Project', models.CharField(max_length=50)),
                ('blog_Summary', models.CharField(max_length=100)),
                ('blog_Content', models.CharField(max_length=1000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
