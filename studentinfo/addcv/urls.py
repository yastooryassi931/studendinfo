from django.urls import path
from . import views


urlpatterns = [

    path('b', views.index, name='index'),
    path('a', views.second, name='second'),
    path('home', views.home, name='home'),
    path('', views.addinfo, name='addinfo'),
    path('show', views.showdata, name='showdata')
]