from django.conf.urls import url

from . import views
from . import ajax

app_name='Exam_portal'

urlpatterns = [
    url(r'^register/$',views.register , name="register"),
    url(r'^instruction/$' ,views.instruction, name="instruction"),
    url(r'^ajaxdisplay/$', ajax.ajax),
    url(r'^show/$',views.show,name="ajaxshow")

]
