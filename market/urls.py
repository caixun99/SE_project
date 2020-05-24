from django.urls import path

from . import views

app_name = 'market'
urlpatterns = [
    path('mall/home/', views.home, name='home'),
    path('mall/sort/', views.sort, name='sort'),
    path('util/error/', views.error, name='error'),
    path('user/profile/', views.profile, name='profile'),
    path('user/article/', views.article, name='article'),
    path('user/community/', views.community, name='community'),
    path('user/buy/', views.buy, name='buy'),
    path('user/sell/', views.sell, name='sell'),
    path('community/groups/', views.groups, name='groups'),
]
