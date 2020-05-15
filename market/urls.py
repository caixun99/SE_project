from django.urls import path

from . import views

app_name = 'market'
urlpatterns = [
    path('mall/home/', views.home, name='home'),
    path('mall/sort/', views.sort, name='sort'),
    path('util/error/', views.error, name='error'),
    path('user/index/', views.index, name='index'),
    path('community/groups/', views.groups, name='groups'),
]
