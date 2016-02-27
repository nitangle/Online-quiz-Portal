from django.conf.urls import url

from . import views

app_name='Exam_portal'

urlpatterns = [
    url(r'^register/$',views.register , name="register"),
]