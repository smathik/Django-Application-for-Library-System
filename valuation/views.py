from django.shortcuts import render
import json
from django.http import HttpResponse
import json
from valuation.models import *
from django.views.decorators.csrf import csrf_exempt
from valuation.models import Family,FamilyMember



def login(request):
    return render(request,'login.html')

def home(request):
    return render(request,'home.html')



def family(request):

    if request.method == 'POST':
        post, data, req_field  = request.POST, {}, ['rationcard' ,'street', 'city', 'code']
        for i in req_field:
            data[i] = post['all[%s]'%i]
            print data
        dump = 'notcomplete' if '' in data.values() else'exists' if Family.objects.filter(ration_card=data['rationcard']) else None             
        if dump:
            print '>>>>>>>>>>>>>>>>>>>>>>>>>>>'
            return HttpResponse(content=json.dumps(dump),content_type='Application/json')
      
        Family.objects.create( ration_card=data['rationcard'], 
                               city=data['city'],
                               street=data['street'],
                               code=data['code'])

    return render(request,'family.html')



        



def members(request):
    if request.method == 'POST':
        post, data, req_field = request.POST, {}, ['rationcard' ,'personcode','name', 'age', 'gender', 'qualification', 'occupation', 'standard', 'institution', 'grade']
        for i in req_field:
            data[i] = post['all[%s]'%i]

        family = Family.objects.filter(ration_card=data['rationcard'])
        studen_field = ['grade', 'institution', 'standard']
        excepttion = [data[i] for i in list(set(req_field)-set(studen_field))]

        dump = 'notcomplete' if '' in excepttion else 'notexists' if not Family.objects.filter(ration_card=data['rationcard']) else 'personcode_not_unique' if FamilyMember.objects.filter(personcode=data['personcode']) else None             
        print 'dump >>', dump
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
                                    grade = data['grade']
                             )

    return render(request,'members.html')

def about(request):
    return render(request,'about.html')

def registration(request):
    return render(request,'registration.html')




def classes(request):
    return render(request,'classes.html')



# def current_datetime(request):
#     now = datetime.datetime.now()
#     return render(request, 'current_datetime.html', {'datetime': now})



def check(request):
    if request.method == 'POST':
        post = request.POST
        personcode = post['code']
        print '>>>>>>>>>>>>>>', personcode
        if not FamilyMember.objects.filter(personcode=personcode):
          data = 'notexists'
        else:
          family = FamilyMember.objects.get(personcode=personcode)
          _class = Classes.objects.get(familymember_id=family.id)
          data = _class.attendance
        print data
        return HttpResponse(content=json.dumps(data),content_type='Application/json')

    return render(request, 'attendancecheck.html')



def classlist(request):

    
    if request.method == 'POST': 
        post = request.POST
        datadump = Classes.objects.all()
        data = [i.subject for i in datadump]
        # print 'ggggggg'
        # classlist.objects.create(subject=sub)
        
       
        return HttpResponse(content=json.dumps({'data': data}),content_type='Application/json')


    return render(request, 'classlist.html')


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
              sub = data_dict['subject']
              classlist = data_dict['classlist']
              time = data_dict['timezone']
            except Exception as e:
              print 'Error>>>>',e

            for i in classlist:
              try:
                name = i['name']
                person_code = i['person_code']
                attendance = i['attendance']
                family = FamilyMember.objects.get(personcode=person_code)
              except Exception as e:
                print 'Error>>>>',e

              Classes.objects.create(familymember_id=family.id, subject=sub, Timing=time, attendance=attendance)
            data = 'saved'
  
        return HttpResponse(content=json.dumps({'data': data}),content_type='Application/json')

    return render(request, 'attendance.html')
