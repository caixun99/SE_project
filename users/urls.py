from django.conf.urls import url
from django.contrib.auth.views import LoginView
from . import views
from django.contrib import admin
from django.urls import path,include,re_path

urlpatterns = [
    re_path(r'^login/$', LoginView.as_view(template_name='users/login.html'), name="login"),
    re_path(r'^logout/$',views.logout_view,name='logout'),
    re_path(r'^register/$',views.register,name='register'),
]