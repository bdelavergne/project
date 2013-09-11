# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Trucks'
        db.create_table(u'trucks_trucks', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'trucks', ['Trucks'])


    def backwards(self, orm):
        # Deleting model 'Trucks'
        db.delete_table(u'trucks_trucks')


    models = {
        u'trucks.trucks': {
            'Meta': {'object_name': 'Trucks'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['trucks']