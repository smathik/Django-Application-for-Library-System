from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from valuation.views import *#home,attendance,members,about,registration,family,classes,login,current_datetime, check
urlpatterns = patterns('',
    # Examples:
    url(r'^$', loginpage),
    url(r'^login/',login_check),
    url(r'^home/', home),
    url(r'^registration/', registration),
    url(r'^about/$',about),
    url(r'^attendance/', attendance),
    url(r'^members/', members),
    url(r'^checkAttendance/', checkAttendance),
    url(r'^classlist/', classlist),
    url(r'^familyedit/',familyedit),
    url(r'^AddEvent/',AddEvent),
    url(r'^addFamilyToEvent/',addFamilyToEvent),
    url(r'^display/',display),
    url(r'^memdis/',memdis),
    url(r'^getMembers/',getMembers),
    url(r'^saveStudentData/',saveStudentData),
    url(r'^getEvents/',getEvents),  
    url(r'^new/',new),
    url(r'^logout',logout_view),
    url(r'^addclass/',addClass),
    url(r'^family/', family),
    url(r'^getStudents/', getStudents),
    url(r'^saveAttendance/', saveAttendance),
    url(r'^ListAllStudents/', ListAllStudents),
    url(r'^DisplayEventFamily/', DisplayEventFamily),


    url(r'^admin/', include(admin.site.urls)),

)
