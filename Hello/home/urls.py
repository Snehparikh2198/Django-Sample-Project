#aa badhi url nakhi and localhost:8000 ma run karyu ae badha ne "UrlDispacher kevay che"
from django.contrib import admin
from django.urls import path

from home import views
urlpatterns = [
    #view.index means ke views vali file ma index function ma jav em.... 
    #and tya jai ne http na lidhe return thai ne print thay gyu...
    path("", views.index, name='home'),
    path("about", views.about, name='about'),
    path("service", views.service, name='service'),
    path("contact", views.contact, name='contact')

]
