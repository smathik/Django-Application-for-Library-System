from django.shortcuts import render
import json
from django.http import HttpResponse
from valuation.models import *
from django.views.decorators.csrf import csrf_exempt
from valuation.models import *
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from datetime import date


def loginpage(request):
  return render(request,'login.html')

def login_check(request):
  username = request.POST['username']
  password = request.POST['password']
  user = authenticate(username=username, password=password)
  if user:
      login(request, user)
      dump = "success"      
      return HttpResponse(content=json.dumps(dump),content_type='Application/json')
  else:
      return render(request,'login.html')

def logout_view(request):
  logout(request)
  return render(request,'login.html')

@login_required
def home(request):
    return render(request,'home.html')

@login_required
def family(request):
      if request.method == 'POST':
        post, data, req_field  = request.POST, {}, ['rationcard' ,'street', 'city', 'code','picture']
        for i in req_field:
            data[i] = post['all[%s]'%i]
        dump = 'notcomplete' if '' in data.values() else 'exists' if Family.objects.filter(ration_card=data['rationcard']) else None       
        if dump:
            return HttpResponse(content=json.dumps(dump),content_type='Application/json')
      
        Family.objects.create( ration_card=data['rationcard'], 
                               street=data['street'],
                               city=data['city'],
                               code=data['code'],
                               picture=data['picture'])
        dump = 'saved'
        return HttpResponse(content=json.dumps(dump),content_type='Application/json')
      return render(request,'family.html')  

@login_required
def about(request):
    return render(request,'about.html')

@login_required
def registration(request):
    return render(request,'registration.html')

@login_required
def classes(request):
    return render(request,'classes.html')

@login_required
def familyedit(request):
    data =[]
    temp = {}
    if request.method == 'POST': 
            post = request.POST
            datadump = Family.objects.all()
            for i in datadump:
              data.append({'ration_card':i.ration_card,'street':i.street,'city':i.city,'code':i.code})
            return HttpResponse(content=json.dumps({'data': data}),content_type='Application/json')
    return render(request,'familyedit.html')



@login_required
def DeleteFamily(request):
  if request.method == 'POST':
      post = request.POST
      ration_card = post['rationid']
      if not Family.objects.filter(ration_card=ration_card):
          data = 'none'
      else:
          obj = Family.objects.get(ration_card=ration_card)
          obj.delete()
          data = 'success'            
      return HttpResponse(content=json.dumps(data),content_type='Application/json')

@login_required
def memdis(request):
    data = []
    if request.method == 'POST':
        post = request.POST
        ration_card = post['ration_card']
        if not Family.objects.filter(ration_card = ration_card):
            data = 'none'    
        else:
            fami = Family.objects.get(ration_card = ration_card)
            datadump = FamilyMember.objects.filter(family = fami)
            for i in datadump:
                data.append({'name':i.name,'Age':i.Age,'Gender':i.Gender,'personcode':i.personcode,'qualification':i.qualification,'occupation':i.occupation,'standard':i.standard,'institution':i.institution,'grade':i.grade})
        return HttpResponse(content=json.dumps(data),content_type='Application/json')
    return render(request, 'memdis.html')

@login_required
def members(request):
    if request.method == 'POST':
        post, data, req_field = request.POST, {}, ['rationcard' ,'personcode','name', 'age', 'gender', 'qualification', 'occupation', 'standard', 'institution', 'grade']
        for i in req_field:
            data[i] = post['all[%s]'%i]
        family = Family.objects.filter(ration_card=data['rationcard'])
        studen_field = ['grade', 'institution', 'standard']
        excepttion = [data[i] for i in list(set(req_field)-set(studen_field))]
 
        dump = 'notcomplete' if '' in excepttion else 'notexists' if not Family.objects.filter(ration_card=data['rationcard']) else 'personcode_not_unique' if FamilyMember.objects.filter(personcode=data['personcode']) else None             
        if dump:
            return HttpResponse(content=json.dumps(dump),content_type='Application/json')
        
        student_check = True if [data[i] for i in studen_field if data[i] != ''] else False
        fam = Family.objects.get(ration_card=data['rationcard']).id
        FamilyMember.objects.create(name = data['name'],
                                    family_id = fam,
                                    personcode = data['personcode'],
                                    Gender = data['gender'],
                                    Age = data['age'],
                                    qualification = data['qualification'],
                                    occupation = data['occupation'],
                                    IsStudent = student_check,
                                    standard = data['standard'], 
                                    institution = data['institution'],
                                    grade = data['grade'],
                                    )
        dump = 'saved'
        return HttpResponse(content=json.dumps(dump),content_type='Application/json')
    return render(request,'members.html')

def addClass(request):
  if request.method == 'POST':
      data = request.POST
      response = 'success'
      if Class.objects.filter(subject=data['subject']):
          response = 'exists'
      else:
          Class.objects.create(subject=data['subject'])
      return HttpResponse(content=json.dumps(response),content_type='Application/json')
  return render(request,'AddClass.html')

@login_required
def attendance(request):
    true, null, false = True, None, False
    if request.method == 'POST':
        post  = request.POST
        if post.has_key('post1'):
            if post.has_key('gender'):
                gender = post['gender']
                datadump = FamilyMember.objects.filter(Gender=gender)
                data = [[i.name, i.personcode] for i in datadump]

            else:
               datadump = FamilyMember.objects.all()
               data = [[i.name, i.personcode] for i in datadump]


       
        elif post.has_key('post2'):
            
            try:
              data_dict = eval(post['data'])
              subject = data_dict['subject']
              classlist = data_dict['classlist']
              time = data_dict['timezone']
            except Exception as e:
              print 'Error>>>>',e

            Classes.objects.create(subject=subject, Timing=time) 
            # Classes.objects.filter(subject=subject)

            sub = Classes.objects.get(subject=subject)
            # print '<<>>><>'




            for i in classlist:
              try:
                name = i['name']
                person_code = i['person_code']
                # attendance = i['attendance']
                family = FamilyMember.objects.get(personcode=person_code)
                family.classname = sub
                family.save()
                print family.classname.__dict__
              except Exception as e:
                print 'Error>>>>',e

            data = 'saved' 
            
            
  
        return HttpResponse(content=json.dumps({'data': data}),content_type='Application/json')

    return render(request, 'attendance.html')

@login_required
def classlist(request):    
    if request.method == 'POST': 
        post = request.POST
        data = [i.subject for i in Class.objects.all()]
        return HttpResponse(content=json.dumps(data),content_type='Application/json')
    return render(request,'classlist.html')

@login_required
def display(request):
        
  if request.method == 'POST':
      post = request.POST
      ration_card = post['rationid']

      if post.has_key('post1'):
          if not Family.objects.filter(ration_card=ration_card):
              data = 'none'
          else:
              obj = Family.objects.get(ration_card=ration_card)
              obj.street = post['street']
              obj.city = post['city']
              obj.code = post['code']
              obj.save()
              data = 'saved'      
      else:
          if not Family.objects.filter(ration_card=ration_card):
              data = 'none'
          else:
              family = Family.objects.get(ration_card=ration_card)
              data = {'ration_card': family.ration_card, 'city': family.city, 'street':family.street, 'code': family.code}
      
      return HttpResponse(content=json.dumps(data),content_type='Application/json')
  return render(request,'display.html')


@login_required
def getEvents(request):
    if request.method == 'POST':
        events = [i.name for i in Event.objects.all()]
        return HttpResponse(content=json.dumps(events),content_type='Application/json')
    return render(request,'Addevents.html')

@login_required
def addFamilyToEvent(request):
      post = request.POST
      event = Event.objects.get(name=post['Event'])
      family = Family.objects.filter(ration_card=post['rationid'])
      if not family:
          response = 'family'
      elif EventData.objects.filter(event=event, family=family[0]):
          response = 'exists'
      else:
          EventData.objects.create(event=event, family=family[0])
          response = 'success'
      return HttpResponse(content=json.dumps(response),content_type='Application/json')

@login_required
def new(request):
  print request.method
  if request.method == 'POST':
    print "inside"
    post = request.POST

    datadump = FamilyMember.objects.all()
    print datadump
    data = [[i.student_list]for i in datadump]
    print data
    return HttpResponse(content=json.dumps(dump),content_type='Application/json')
  else:
    return render(request,'new.html')

@login_required
def getMembers(request):
    members = [{'name': i.name, 'personcode': i.personcode} for i in FamilyMember.objects.all()]
    return HttpResponse(content=json.dumps(members),content_type='Application/json')

@login_required
def getStudents(request):
    classname = request.POST['classname']
    students = [{'name': i.student.name, 'personcode': i.student.personcode} for i in StudentClass.objects.filter(classname=Class.objects.get(subject=classname))]
    return HttpResponse(content=json.dumps(students),content_type='Application/json')

@login_required
def saveAttendance(request):
    post = request.POST
    data_dict = eval(post['data'])
    classname = data_dict['classname']
    studentData = data_dict['studentData']
    ClasS = Class.objects.filter(subject=classname)

    if not Attendance.objects.filter(classname=ClasS[0], date=date.today().strftime('%Y-%m-%d')):
        for i in studentData:
            name, personcode = i.split(' ')
            student = FamilyMember.objects.get(personcode=personcode)
            Attendance.objects.create(classname=ClasS[0], student=student, attendance=True)
        response = 'success'
    else:
        response = 'exists'
    return HttpResponse(content=json.dumps(response),content_type='Application/json')  

@login_required
def saveStudentData(request):
    post = request.POST
    data_dict = eval(post['data'])
    classname = data_dict['classname']
    studentData = data_dict['studentData']
    
    if not Class.objects.filter(subject=classname):
        Class.objects.create(subject=classname)
        ClasS = Class.objects.get(subject=classname)      
        for i in studentData:
            name, personcode = i.split(' ')
            student = FamilyMember.objects.get(personcode=personcode)
            StudentClass.objects.create(classname=ClasS, student=student)
        response = 'success'
    else:
        response = 'exists'
    return HttpResponse(content=json.dumps(response),content_type='Application/json')    

@login_required
def AddEvent(request):
    if request.method == 'POST':
        event = request.POST['eventName']
        response = 'success'
        if Event.objects.filter(name=event):
            response = 'exists'
        else:
            Event.objects.create(name=event)
        return HttpResponse(content=json.dumps(response),content_type='Application/json')
    return render(request,'events.html')

@login_required
def checkAttendance(request):
    if request.method == 'POST':
        post = request.POST
        print post
        student = FamilyMember.objects.filter(personcode=post['code'])
        response = True
        if not student:
            response = 'notexists'
        else: 
            ClasS = Class.objects.get(subject=post['Class'])
            month = int(post['month'])
            day = int(post['day'])
            month = '0%s'%month if month<10 else month
            day = '0%s'%day if day<10 else day            
            date = '%s-%s-%s'%(post['year'],month,day)
            print date
            Check = Attendance.objects.filter(classname=ClasS, student=student[0], date=date)
            if Check:
                response = True
            else:
                response = False
            print response
        return HttpResponse(content=json.dumps(response),content_type='Application/json')
    return render(request, 'attendancecheck.html')

@login_required
def ListAllStudents(request):
    if request.method == 'POST':
        post = request.POST
        print post
        ClasS = Class.objects.get(subject=post['classname'])
        month = int(post['month'])
        day = int(post['day'])
        month = '0%s'%month if month<10 else month
        day = '0%s'%day if day<10 else day            
        date = '%s-%s-%s'%(post['year'],month,day)
        AllStudents = [{'name': i.student.name, 'personcode': i.student.personcode} for i in  Attendance.objects.filter(classname=ClasS, date=date)]
    return HttpResponse(content=json.dumps(AllStudents),content_type='Application/json')

@login_required
def DisplayEventFamily(request):
    if request.method == 'POST':
        events = [i.family.ration_card for i in EventData.objects.filter(event=Event.objects.get(name=request.POST['Event']))]
        return HttpResponse(content=json.dumps(events),content_type='Application/json')        
    return render(request, 'displayEventFamily.html')


