from django.conf.urls import url
import rest_framework_jwt.views
import djoser.views
from attendence import views

urlpatterns = [
    url(r'^auth/login', rest_framework_jwt.views.obtain_jwt_token),
    # Uncomment the below lines only if not using JWT
    #url(r'^auth/login', djoser.views.LoginView.as_view()),
    #url(r'^auth/logout', djoser.views.LogoutView.as_view()),
    url(r'^auth/me', djoser.views.UserView.as_view()),
    url(r'^auth/register', djoser.views.RegistrationView.as_view()),
    url(r'^students/$', views.StudentList.as_view()),
    url(r'^students/(?P<pk>[0-9]+)/$', views.StudentDetail.as_view()),
    url(r'^subjectholder/(?P<branch>[0-9]+)/(?P<semester>[0-9]+)/$', views.SubjectHolderList.as_view()),
    url(r'^subjects/$', views.SubjectList.as_view()),
    url(r'^subjects/(?P<pk>[0-9]+)/$', views.SubjectDetail.as_view()),
    url(r'^attendance/$', views.AttendanceList.as_view()),
    url(r'^attendance/(?P<pk>[0-9]+)/$', views.AttendanceDetail.as_view()),
    url(r'^attendance/(?P<branch>[0-9]+)/(?P<semester>[0-9]+)/$', views.AttendanceList.as_view()),
]
