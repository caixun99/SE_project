from django.urls import path,re_path

from . import views

app_name = 'market'
urlpatterns = [
    #re_path(r'^category/(\d+)/$',views.category,name='category'),
    re_path(r'^community//$',views.community,name='community'),
    re_path(r'^dynamics/(?P<dynamic_id>\d+)/$',views.dynamic,name='dynamic'),
    re_path(r'^community/(?P<kind_id>\d+)/$',views.dynamics,name='dynamics'),
    re_path(r'^new_dynamic/(?P<kind_id>\d+)$',views.new_dynamic,name='new_dynamic'),
    re_path(r'^new_comment/(?P<dynamic_id>\d+)/$',views.new_comment,name='new_comment'),
    re_path(r'^edit_comment/(?P<comment_id>\d+)/$',views.edit_comment,name='edit_comment'),
    path('',views.index,name='index'),
]
