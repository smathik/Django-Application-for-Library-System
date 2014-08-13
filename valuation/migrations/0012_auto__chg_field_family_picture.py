# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Family.picture'
        db.alter_column(u'valuation_family', 'picture', self.gf('django.db.models.fields.TextField')(default=None))

    def backwards(self, orm):

        # Changing field 'Family.picture'
        db.alter_column(u'valuation_family', 'picture', self.gf('django.db.models.fields.TextField')(null=True))

    models = {
        u'valuation.attendance': {
            'Meta': {'object_name': 'Attendance'},
            'attendance': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'classname': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['valuation.Class']"}),
            'date': ('django.db.models.fields.CharField', [], {'default': "'2014-08-12'", 'max_length': '11'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['valuation.FamilyMember']"})
        },
        u'valuation.class': {
            'Meta': {'object_name': 'Class'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'valuation.event': {
            'Meta': {'object_name': 'Event'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'valuation.eventdata': {
            'Meta': {'object_name': 'EventData'},
            'date': ('django.db.models.fields.CharField', [], {'default': "'2014-08-12'", 'max_length': '11'}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['valuation.Event']"}),
            'family': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['valuation.Family']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'valuation.family': {
            'Meta': {'object_name': 'Family'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'code': ('django.db.models.fields.IntegerField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'picture': ('django.db.models.fields.TextField', [], {}),
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
        },
        u'valuation.studentclass': {
            'Meta': {'object_name': 'StudentClass'},
            'classname': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['valuation.Class']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['valuation.FamilyMember']", 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['valuation']