# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Classes'
        db.create_table(u'valuation_classes', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('familymember', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['valuation.FamilyMember'])),
            ('subject', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('Timing', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('attendance', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'valuation', ['Classes'])


    def backwards(self, orm):
        # Deleting model 'Classes'
        db.delete_table(u'valuation_classes')


    models = {
        u'valuation.classes': {
            'Meta': {'object_name': 'Classes'},
            'Timing': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'attendance': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'familymember': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['valuation.FamilyMember']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'valuation.classlist': {
            'Meta': {'object_name': 'classlist'},
            'attendance': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'classname': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'valuation.events': {
            'Meta': {'object_name': 'events'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'valuation.eventssave': {
            'Meta': {'object_name': 'eventssave'},
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'events': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['valuation.events']"}),
            'family': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['valuation.Family']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'valuation.family': {
            'Meta': {'object_name': 'Family'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'code': ('django.db.models.fields.IntegerField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'ration_card': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'valuation.familymember': {
            'Age': ('django.db.models.fields.IntegerField', [], {'max_length': '50'}),
            'Gender': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'IsStudent': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'Meta': {'object_name': 'FamilyMember'},
            'family': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['valuation.Family']"}),
            'grade': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'institution': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'occupation': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'personcode': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'qualification': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'standard': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['valuation']