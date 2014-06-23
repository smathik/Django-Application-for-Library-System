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

# def familydisplay(request):
#     if request.method == 'GET':
#         get, data, req_field , get = request.POST, {}, ['rationcard' ,'street', 'city', 'code']
#         for i in req_field:
#             data[i] = get['all[%s]'%i]
#         print data

#     return render(request,'familydisplay.html')
        
def attendance(request):
    if request.method == 'POST':
        post  = request.POST,{}, ['subject','timings','attendance']
        for i in req_field:
            data[i] = post['all[%s]'%i]
            print data
        if post.has_key('gender'):
            gender = post['gender']
            datadump = FamilyMember.objects.filter(Gender=gender)
            data = [[i.name, i.personcode] for i in datadump]

        else:
           datadump = FamilyMember.objects.all()
           data = [[i.name, i.personcode] for i in datadump]


        attendance.objects.create( subject=data['subject'],
                                   timings=data['timings'],
                                   attendance=data['attendance'])
  
        return HttpResponse(content=json.dumps({'data': data}),content_type='Application/json')

    return render(request, 'attendance.html')

# # subject = request.POST.get('subject')
     # # morning = request.POST.get('morning')
     # # evening = request.POST.get('evening')
     # # students = request.POST.get('students')
     # # for _id, attend in students.items():
     #     
     #                          morning = data['morning'], 
     #                          evening = data['evening'], 
     #                          member_id = data['member_id'], 
     #                          attendance = data['attendance']   )
    
    


def members(request):
    if request.method == 'POST':
        post, data, req_field = request.POST, {}, ['rationcard' ,'personcode','name', 'age', 'gender', 'qualification', 'occupation', 'standard', 'institution', 'grade']
        for i in req_field:
            data[i] = post['all[%s]'%i]

        family = Family.objects.filter(ration_card=data['rationcard'])
        studen_field = ['grade', 'institution', 'standard']
        excepttion = [data[i] for i in list(set(req_field)-set(studen_field))]

        dump = 'notexists' if not Family.objects.filter(ration_card=data['rationcard']) else 'notcomplete' if '' in excepttion else None             
        print dump
        if dump:
            # print '????????????????????????????'
            return HttpResponse(content=json.dumps(dump),content_type='Application/json')
        
        student_check = True if [data[i] for i in studen_field if data[i] != ''] else False
        # print student_check
        fam = Family.objects.get(ration_card=data['rationcard']).id
        # print data
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



def current_datetime(request):
    now = datetime.datetime.now()
    return render(request, 'current_datetime.html', {'datetime': now})




