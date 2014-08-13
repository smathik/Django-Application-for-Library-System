from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
admin.autodiscover()

from valuation.views import *
urlpatterns = patterns('',
   
    url(r'^$', loginpage),
    url(r'^login/',login_check),
    url(r'^home/', home),
    url(r'^registration/', registration),
    url(r'^about/$',about),
    url(r'^attendance/', attendance),
    url(r'^members/', members),
    url(r'^checkAttendance/', checkAttendance),
    url(r'^classlist/', classlist),
    url(r'^familydisplay/',familydisplay),
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
    url(r'^DeleteFamily/', DeleteFamily),
    url(r'^rationid_details/', rationid_details),
    # url(r'^family_pic/', family_pic),
    # url(r'^sample/', sample),
    # urlpatterns += staticfiles_urlpatterns()
    # urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
        

    url(r'^admin/', include(admin.site.urls)),

) 
# * static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
