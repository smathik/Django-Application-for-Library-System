# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Family'
        db.create_table(u'valuation_family', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ration_card', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('street', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('code', self.gf('django.db.models.fields.IntegerField')(max_length=50)),
            ('picture', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'valuation', ['Family'])

        # Adding model 'FamilyMember'
        db.create_table(u'valuation_familymember', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('personcode', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('family', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['valuation.Family'])),
            ('Gender', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('Age', self.gf('django.db.models.fields.IntegerField')(max_length=50)),
            ('qualification', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('occupation', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('IsStudent', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('standard', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('institution', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('grade', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
        ))
        db.send_create_signal(u'valuation', ['FamilyMember'])

        # Adding model 'Class'
        db.create_table(u'valuation_class', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('subject', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'valuation', ['Class'])

        # Adding model 'StudentClass'
        db.create_table(u'valuation_studentclass', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('classname', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['valuation.Class'])),
            ('student', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['valuation.FamilyMember'], null=True, blank=True)),
        ))
        db.send_create_signal(u'valuation', ['StudentClass'])

        # Adding model 'Attendance'
        db.create_table(u'valuation_attendance', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('classname', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['valuation.Class'])),
            ('student', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['valuation.FamilyMember'])),
            ('attendance', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('date', self.gf('django.db.models.fields.CharField')(default='2014-08-09', max_length=11)),
        ))
        db.send_create_signal(u'valuation', ['Attendance'])

        # Adding model 'Event'
        db.create_table(u'valuation_event', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'valuation', ['Event'])

        # Adding model 'EventData'
        db.create_table(u'valuation_eventdata', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('event', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['valuation.Event'])),
            ('family', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['valuation.Family'])),
            ('date', self.gf('django.db.models.fields.CharField')(default='2014-08-09', max_length=11)),
        ))
        db.send_create_signal(u'valuation', ['EventData'])


    def backwards(self, orm):
        # Deleting model 'Family'
        db.delete_table(u'valuation_family')

        # Deleting model 'FamilyMember'
        db.delete_table(u'valuation_familymember')

        # Deleting model 'Class'
        db.delete_table(u'valuation_class')

        # Deleting model 'StudentClass'
        db.delete_table(u'valuation_studentclass')

        # Deleting model 'Attendance'
        db.delete_table(u'valuation_attendance')

        # Deleting model 'Event'
        db.delete_table(u'valuation_event')

        # Deleting model 'EventData'
        db.delete_table(u'valuation_eventdata')


    models = {
        u'valuation.attendance': {
            'Meta': {'object_name': 'Attendance'},
            'attendance': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'classname': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['valuation.Class']"}),
            'date': ('django.db.models.fields.CharField', [], {'default': "'2014-08-09'", 'max_length': '11'}),
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
            'date': ('django.db.models.fields.CharField', [], {'default': "'2014-08-09'", 'max_length': '11'}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['valuation.Event']"}),
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
        },
        u'valuation.studentclass': {
            'Meta': {'object_name': 'StudentClass'},
            'classname': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['valuation.Class']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['valuation.FamilyMember']", 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['valuation']