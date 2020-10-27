"""Hello URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""




from django.contrib import admin
from django.urls import path,include

admin.site.site_header = "Utsav Admin"
admin.site.site_title = "Utsav Admin Portal"
admin.site.index_title = "Welcome to Utsav Researcher Portal"

urlpatterns = [
    #koi pan localhost ma admin/ lakhe to django admin ma jay evu.. I means ke django admistrinition ma jay evu
    path('admin/', admin.site.urls), 
    
    #Home url ma jav 
    path('',include('home.urls'))


]
