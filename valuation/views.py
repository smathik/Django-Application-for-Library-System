from django.shortcuts import render
import json
from django.http import HttpResponse
import json
from valuation.models import *
from django.views.decorators.csrf import csrf_exempt
from valuation.models import Family,FamilyMember,events



def login(request):
    return render(request,'login.html')

def home(request):
    return render(request,'home.html')



def family(request):

      if request.method == 'POST':
        post, data, req_field  = request.POST, {}, ['rationcard' ,'street', 'city', 'code','picture']
        for i in req_field:
            data[i] = post['all[%s]'%i]
            print data
        
                
            
        dump = 'notcomplete' if '' in data.values() else 'exists' if Family.objects.filter(ration_card=data['rationcard']) else None       

 
        

        if dump:
            print '>>>>>>>>>>>>>>>>>>>>>>>>>>>'
            return HttpResponse(content=json.dumps(dump),content_type='Application/json')
      
        Family.objects.create( ration_card=data['rationcard'], 
                               street=data['street'],
                               city=data['city'],
                               code=data['code'],
                               picture=data['picture'])

        dump = 'saved'
        return HttpResponse(content=json.dumps(dump),content_type='Application/json')


      return render(request,'family.html')  


        





def about(request):
    return render(request,'about.html')

def registration(request):
    return render(request,'registration.html')




def classes(request):
    return render(request,'classes.html')



# def current_datetime(request):
#     now = datetime.datetime.now()
#     return render(request, 'current_datetime.html', {'datetime': now})
#     return render(request, 'classlist.html')

def display(request):
        
  if request.method == 'POST':
      post = request.POST
      ration_card = post['rationid']
     
      if post.has_key('post1'):
          try:
            obj = Family.objects.get(ration_card=ration_card)
          except Exception as e:
            print e
         
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
              print data    
      
      return HttpResponse(content=json.dumps(data),content_type='Application/json')

  return render(request,'display.html')

def members(request):
    if request.method == 'POST':
        post, data, req_field = request.POST, {}, ['rationcard' ,'personcode','name', 'age', 'gender', 'qualification', 'occupation', 'standard', 'institution', 'grade']
        for i in req_field:
            data[i] = post['all[%s]'%i]

        family = Family.objects.filter(ration_card=data['rationcard'])
        nam = Classes.objects.get(subject=data['subject'])
        student_list = FamilyMember.objects.filter(classname = nam)
        studen_field = ['grade', 'institution', 'standard']
        excepttion = [data[i] for i in list(set(req_field)-set(studen_field))]

        dump = 'notcomplete' if '' in excepttion else 'notexists' if not Family.objects.filter(ration_card=data['rationcard']) else 'personcode_not_unique' if FamilyMember.objects.filter(personcode=data['personcode']) else None             
        print 'dump >>>>', dump
        if dump:
            return HttpResponse(content=json.dumps(dump),content_type='Application/json')
        
        student_check = True if [data[i] for i in studen_field if data[i] != ''] else False
        fam = Family.objects.get(ration_card=data['rationcard']).id
        FamilyMember.objects.create(name = data['name'],
                                    family_id = fam,
                                    personcode = data['personcode'],
                                    Gender = data['gender'],
                                    age = data['age'],
                                    qualification = data['qualification'],
                                    occupation = data['occupation'],
                                    IsStudent = student_check,
                                    standard = data['standard'], 
                                    institution = data['institution'],
                                    grade = data['grade'],
                                    classname = nam,  
                             )
        dump = 'saved'
        return HttpResponse(content=json.dumps(dump),content_type='Application/json')

    return render(request,'members.html')



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

def classlist(request):

    
    if request.method == 'POST': 
        post = request.POST
        datadump = Classes.objects.all()
        data = [[i.subject]for i in datadump]
        # mem = FamilyMember.objects.get(classname=name)
        # print mem

        # print 'ggggggg'
        # classlist.objects.create(subject=sub)
        
       
        return HttpResponse(content=json.dumps({'data': data}),content_type='Application/json')
    return render(request,'classlist.html')

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

def new_get(request):
    print request.method

    print "inside"
    post = request.POST
    nam = Classes.objects.get(subject=post['student_list'])
    student_list = FamilyMember.objects.filter(classname = nam)
  # datadump = FamilyMember.objects.filter(classname =)
  # print datadump
  # dump = [[i.student_list]for i in datadump]
  # dump = student_list
    print student_list
    # datadump = student_list
    # print data
    dump =[]
    for i in student_list:
      i.name
      dump.append(i.name)
    return HttpResponse(content=json.dumps(dump),content_type='Application/json')












 # Classes.objects.create(familymember_id=data['familymember_id'],
 #                                     subject=data['subject'], 
 #                                     Timing=data['Timing'],
 #                                     attendance=data['attendance'])







def Addevents(request):
  if request.method == 'POST':
    post, data, req_field = request.POST, {}, ['rationcard', 'name']
    for i in req_field:
      data[i] = post['all[%s]'%i]
    # family = Family.objects.filter(ration_card=data['rationcard'])
    # name = events.objects.filter(name=data['name'])
    # if dump:
      
    #   return HttpResponse(content=json.dumps(dump),content_type='Application/json')
    fam = Family.objects.get(ration_card=data['rationcard'])

    nam = events.objects.get(name=data['name'])
    eventssave.objects.create( family = fam,
                              events = nam )
    dump = 'saved'

    return HttpResponse(content=json.dumps(dump),content_type='Application/json')
  return render(request,'Addevents.html')





def event(request):
    if request.method == 'POST':
      post, data, req_field = request.POST, {}, ['name']
      for i in req_field: 
        data[i] = post['all[%s]'%i]
        print data
      dump = 'saved'
      try:
        events.objects.create(name=data['name'])
      except Exception as e:
        print e
      return HttpResponse(content=json.dumps(dump),content_type='Application/json')
    return render(request,'events.html')


def memdis(request):
    data = []
    temp = {}
    if request.method == 'POST':
       post = request.POST
       datadump = FamilyMember.objects.all()
       for i in datadump:
          data.append({'name':i.name,'Age':i.Age,'Gender':i.Gender,'personcode':i.personcode,'qualification':i.qualification,'occupation':i.occupation,'standard':i.standard,'institution':i.institution,'grade':i.grade})
          print data
       return HttpResponse(content=json.dumps(({'data': data})),content_type='Application/json')
    return render(request, 'memdis.html')


def familyedit(request):
    data =[]
    temp = {}
    if request.method == 'POST': 
            post = request.POST
            datadump = Family.objects.all()
            # data = i.__dict__ for i in datadump
            for i in datadump:
              data.append({'ration_card':i.ration_card,'street':i.street,'city':i.city,'code':i.code})
            # data = [[i.rationcard][i.street][i.city][i.code]for i in datadump]          


            # for i in datadump:
            #   for j in i.__dict__:
            #     if j != '_state':
            #       temp[j] = i.__dict__[j]
            #   data.append(temp)
            # print data


            return HttpResponse(content=json.dumps({'data': data}),content_type='Application/json')
    return render(request,'familyedit.html')




def check(request):
    if request.method == 'POST':
        post = request.POST
        personcode = post['code']
        print '>>>>>>>>>>>>>>', personcode
        if not FamilyMember.objects.filter(personcode=personcode):
          data = 'notexists' 
        else:
          family = FamilyMember.objects.get(personcode=personcode)
          _class = Classes.objects.filter(familymember_id=family.id)[0]
          data = _class.attendance
        print data
        return HttpResponse(content=json.dumps(data),content_type='Application/json')

    return render(request, 'attendancecheck.html')

