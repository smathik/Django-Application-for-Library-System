from django.db import models





class Family(models.Model):	
	ration_card = models.CharField(max_length=50)
	city = models.CharField(max_length=50)
	street = models.CharField(max_length=50)
	code = models.IntegerField(max_length=50)
	picture = models.ImageField(upload_to='gallery')

	


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
    

class classlist(models.Model):
	classname = models.CharField(max_length=50)
	studentlist = models.CharField(max_length=50)
	# studentlist = models.ForeignKey('attendance')


# class events(models.model):
# 	name = models.CharField(max_length=50)

# class eventssave(models.model):
# 	events = models.ForeignKey('events')
# 	family = models.ForeignKey('Family')
	
	






# class gallery(models.Model):
# 	pictures = models.ManyToManyField(Picture)

# class Attendance(models.Model):
# 	date = models.DateTimeField(auto_now_add=True)
# 	classcode = models.ForeignKey('Classes')
# 	# member = models.ForeignKey('StudentDetails')
# 	attendance = models.BooleanField(default=False)

# class Foods(model.Models):
# 	attendance = models.ForeignKey('Family_mem')
# 	stocks = models.IntegerField(max_length=100000)
	 
