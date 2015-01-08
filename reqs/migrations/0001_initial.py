# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='VerseRequest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=80)),
                ('body', models.TextField()),
                ('dest', models.ForeignKey(related_name='received', to=settings.AUTH_USER_MODEL)),
                ('parent', models.ForeignKey(related_query_name=b'child', related_name='children', blank=True, to='reqs.VerseRequest', null=True)),
                ('src', models.ForeignKey(related_name='sent', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
