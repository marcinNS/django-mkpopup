# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0012_auto_20150607_2207'),
    ]

    operations = [
        migrations.CreateModel(
            name='MkPopup',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('popup_contain', models.TextField(null=True, blank=True)),
                ('popup_image', models.ImageField(null=True, blank=True, upload_to='popup')),
                ('popup_url', models.URLField(null=True, blank=True, max_length=250)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Popup',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(serialize=False, parent_link=True, to='cms.CMSPlugin', primary_key=True, auto_created=True)),
                ('mkpopup', models.ForeignKey(to='django_mkpopup.MkPopup')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
