# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('text', models.TextField(verbose_name='Полное содержание')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата создания')),
                ('published_date', models.DateTimeField(null=True, blank=True, verbose_name='Дата публикации')),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='автор')),
            ],
            options={
                'verbose_name': 'статья блога',
                'verbose_name_plural': 'статьи блога',
                'ordering': ['-published_date'],
            },
        ),
    ]
