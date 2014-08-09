from django.db import models
from datetime import date

class Family(models.Model):	
	ration_card = models.CharField(max_length=50)
	city = models.CharField(max_length=50)
	street = models.CharField(max_length=50)
	code = models.IntegerField(max_length=50)
	picture = models.ImageField(upload_to='/home/smathik/family/gallery')

class FamilyMember(models.Model):
	name = models.CharField(max_length=50)
	personcode = models.CharField(max_length=50)
	family = models.ForeignKey('Family')
	Gender = models.CharField(max_length=50)
	Age = models.IntegerField(max_length=50)
	qualification = models.CharField(max_length=50)
	occupation = models.CharField(max_length=50)
	IsStudent = models.BooleanField(default=False)
	standard = models.CharField(max_length=50, null=True, blank=True)
	institution = models.CharField(max_length=50, null=True, blank=True)
	grade = models.CharField(max_length=50, null=True, blank=True)

class Class(models.Model):
	subject = models.CharField(max_length=50)
	
class StudentClass(models.Model):
	classname = models.ForeignKey('Class')
	student = models.ForeignKey('FamilyMember', null=True, blank=True)

class Attendance(models.Model):
	def Date():
		return date.today().strftime('%Y-%m-%d')
	classname = models.ForeignKey('Class')
	student = models.ForeignKey('FamilyMember')
	attendance = models.BooleanField(default=False)
	date = models.CharField(max_length=11, default=Date)
			
class Event(models.Model):
	name = models.CharField(max_length=50)

class EventData(models.Model):
	def Date():
		return date.today().strftime('%Y-%m-%d')
	event = models.ForeignKey('Event')
	family = models.ForeignKey('Family')
	date = models.CharField(max_length=11, default=Date)
	
	
	