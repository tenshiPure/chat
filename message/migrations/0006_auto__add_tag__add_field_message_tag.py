# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Tag'
        db.create_table(u'message_tag', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('body', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('updateDate', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'message', ['Tag'])

        # Adding field 'Message.tag'
        db.add_column(u'message_message', 'tag',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['message.Tag'], null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Tag'
        db.delete_table(u'message_tag')

        # Deleting field 'Message.tag'
        db.delete_column(u'message_message', 'tag_id')


    models = {
        u'message.message': {
            'Meta': {'object_name': 'Message'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'datetime': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ref': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['message.Message']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['message.Tag']", 'null': 'True', 'blank': 'True'})
        },
        u'message.tag': {
            'Meta': {'object_name': 'Tag'},
            'body': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'updateDate': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['message']