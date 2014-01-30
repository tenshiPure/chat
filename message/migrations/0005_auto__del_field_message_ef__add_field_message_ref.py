# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Message.ef'
        db.delete_column(u'message_message', 'ef_id')

        # Adding field 'Message.ref'
        db.add_column(u'message_message', 'ref',
                      self.gf('django.db.models.fields.related.OneToOneField')(to=orm['message.Message'], unique=True, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Message.ef'
        db.add_column(u'message_message', 'ef',
                      self.gf('django.db.models.fields.related.OneToOneField')(to=orm['message.Message'], unique=True, null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Message.ref'
        db.delete_column(u'message_message', 'ref_id')


    models = {
        u'message.message': {
            'Meta': {'object_name': 'Message'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'datetime': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ref': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['message.Message']", 'unique': 'True', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['message']