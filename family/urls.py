from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from valuation.views import *#home,attendance,members,about,registration,family,classes,login,current_datetime, check
urlpatterns = patterns('',
    # Examples:
    url(r'^$', login),
    url(r'^home/', home),
    url(r'^registration/', registration),
    url(r'^about/$',about),
    url(r'^attendance/', attendance),
    url(r'^members/', members),
    url(r'^check/', check),
    url(r'^classlist/', classlist),
    url(r'^familyedit/',familyedit),
    url(r'^events/',event),
    url(r'^Addevents/',Addevents),
    url(r'^display/',display),


    
    # url(r'^familydisplay/', familydisplay),
    # url(r'^time/$',current_datetime),
    
    
    url(r'^family/', family),
    url(r'^classes/', classes),
    # url(r'^qualification/', qualification),


    

    url(r'^admin/', include(admin.site.urls)),

)
