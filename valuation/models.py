from django.db import models

# Create your models here.



class Family(models.Model):	
	ration_card = models.CharField(max_length=50)
	# member_details = models.ManyToManyField('Family_mem')
	city = models.CharField(max_length=50)
	street = models.CharField(max_length=50)
	code = models.IntegerField(max_length=50)

	# family = models.ForeignKey('Family')
	# family_mem = models.ManyToMany('Family_mem')
	# card_no = models.IntegerField(max_length=200)
	# income = models.IntegerField(max_length=50)
	# address = models.CharField(max_length=50)
	# attendance = models.Primarykey('Attendance')
	# address = models.ForeignKey('Address')
	# ration_card = models.URLField()


class FamilyMember(models.Model):
	name = models.CharField(max_length=50)
	personcode = models.CharField(max_length=50)
	family = models.ForeignKey('Family')
	Gender = models.CharField(max_length=50)
	Age = models.IntegerField(max_length=50)
	qualification = models.CharField(max_length=50)
	occupation = models.CharField(max_length=50)
	# income = models.IntegerField(max_length=50)
	IsStudent = models.BooleanField(default=False)
	standard = models.CharField(max_length=50, null=True, blank=True)
	institution = models.CharField(max_length=50, null=True, blank=True)
	grade=models.CharField(max_length=50, null=True, blank=True)


# class StudentDetails(models.Model):
# 	# student = models.OneToOne('IsStudent')
	# standard = models.CharField(max_length=50)
	# institution = models.CharField(max_length=50)
	# grade=models.CharField(max_length=50)


class Classes(models.Model):
	familymember = models.ForeignKey('FamilyMember')
	subject = models.CharField(max_length=50)
	Timing = models.CharField(max_length=50)
	attendance = models.BooleanField(default=False)	
    


# class Attendance(models.Model):
# 	date = models.DateTimeField(auto_now_add=True)
# 	classcode = models.ForeignKey('Classes')
# 	# member = models.ForeignKey('StudentDetails')
# 	attendance = models.BooleanField(default=False)

# class Foods(model.Models):
# 	attendance = models.ForeignKey('Family_mem')
# 	stocks = models.IntegerField(max_length=100000)
	 
