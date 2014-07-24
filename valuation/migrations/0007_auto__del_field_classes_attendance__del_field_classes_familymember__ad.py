# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Classes.attendance'
        db.delete_column(u'valuation_classes', 'attendance')

        # Deleting field 'Classes.familymember'
        db.delete_column(u'valuation_classes', 'familymember_id')

        # Adding field 'FamilyMember.classname'
        db.add_column(u'valuation_familymember', 'classname',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=2, to=orm['valuation.Classes']),
                      keep_default=False)

        # Adding field 'FamilyMember.attendance'
        db.add_column(u'valuation_familymember', 'attendance',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Classes.attendance'
        db.add_column(u'valuation_classes', 'attendance',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Classes.familymember'
        raise RuntimeError("Cannot reverse this migration. 'Classes.familymember' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Classes.familymember'
        db.add_column(u'valuation_classes', 'familymember',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['valuation.FamilyMember']),
                      keep_default=False)

        # Deleting field 'FamilyMember.classname'
        db.delete_column(u'valuation_familymember', 'classname_id')

        # Deleting field 'FamilyMember.attendance'
        db.delete_column(u'valuation_familymember', 'attendance')


    models = {
        u'valuation.classes': {
            'Meta': {'object_name': 'Classes'},
            'Timing': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
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
            'attendance': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'classname': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['valuation.Classes']"}),
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
        u'valuation.new': {
            'Meta': {'object_name': 'new'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        }
    }

    complete_apps = ['valuation']