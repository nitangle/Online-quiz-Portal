from django.conf.urls import url

from . import views
from . import ajax

app_name='Exam_portal'

urlpatterns = [
    url(r'^register/$',views.register , name="register"),
    url(r'^instruction/$' ,views.instruction, name="instruction"),
    url(r'^show/$',views.show,name="ajaxshow"),
    url(r'^next/$',ajax.ajaxnext, name="ajaxnext"),
    url(r'^previous/$',ajax.ajaxprevious, name="ajaxprevious"),
    url(r'^postajax/$',ajax.postajax, name="postajax"),
    url(r'^grid/$',ajax.grid,name="ajaxgrid"),
    url(r'^timer/$', views.timer, name='timer'),
    url(r'^end/$', views.end, name="end"),
    url(r'^admin/$' ,views.admin , name="admin"),
    url(r'^edit/$' ,views.edit_question, name="edit_question"),
    url(r'^update_question/$',ajax.question_update,name="question_update"),
    url(r'^delete/$' , ajax.delete , name="delete"),
    url(r'^adminchoice/$', views.adminchoice , name="adminchocie"),
    url(r'^edittime/$' , views.edittime ,name="edittime"),
    url(r'^student_section/$' , views.student_section, name="student"),
    url(r'^adminLogin/$' , views.admin_auth , name="admin_auth"),
    url(r'^adminLogout/$' , views.logout_admin, name="logout_admin")
]
