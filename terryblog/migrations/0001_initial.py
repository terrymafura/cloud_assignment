# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PostEntry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('hero_image', models.ImageField(upload_to=b'terryblog/media/')),
                ('post_body', models.TextField()),
                ('post_image', models.ImageField(upload_to=b'terryblog/media/', blank=True)),
                ('author', models.CharField(max_length=30)),
                ('created', models.DateTimeField(verbose_name=b'date published')),
                ('slug', models.SlugField(unique=True, max_length=200)),
                ('published', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='PostTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tag', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='postentry',
            name='tags',
            field=models.ManyToManyField(to='terryblog.PostTag'),
        ),
    ]
