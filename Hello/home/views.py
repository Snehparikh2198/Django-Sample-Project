#render che su to ae template ne render karva mate... 
#aani ander 2 concept hoi che ek static file concept and second is template file concept

#Static file ma all images ae badhu aavse.. static file means evi file je badha aapda url ma aai ne joi le evu..
#Hello folder ma setting.py file ni ander STATIC_URL = '/static/' aa code che cheele toh ae ena mate j che evu... 
#static file ma koi divas badha data na nakhvo becoz badha ne ae dekhay etle

#python manage.py makemigrations
#No changes detected

# python manage.py migrate admin mate
#admin karsu to error aavse toh ena mate ek super user bannvu padse to ena mate no code niche che..
#super user mate python manage.py createsuperuser karvu..ena pachi aavu aavse
# Username (leave blank to use 'dell'): admin
# Email address:
# Password: admin
# Password (again):admin
# This password is too short. It must contain at least 8 characters.
# This password is too common.
# Bypass password validation and create user any way? [y/N]: y
# Superuser created successfully.

#aa thaya pachi localhost ma jai ne pachad /admin kari ne id password adminnakhva to ae aavse and jo uper djnago admistirnation chnage karvu hoi toh 
#https://books.agiliq.com/projects/django-admin-cookbook/en/latest/change_text.html aa link par jai ne admin.site.site_header = "UMSRA Admin"
# admin.site.site_title = "UMSRA Admin Portal"
# admin.site.index_title = "Welcome to UMSRA Researcher Portal" 
# from django.shortcuts import render, HttpResponse aane hello/ ma urls.py ma nakhvu


#aanathi deatils male evu..
# python manage.py shell 

# Python 3.7.1 (default, Dec 10 2018, 22:54:23) [MSC v.1915 64 bit (AMD64)]
# Type 'copyright', 'credits' or 'license' for more information
# IPython 7.2.0 -- An enhanced Interactive Python. Type '?' for help.

# In [1]: from home.models import Contact

# In [2]: from home.models import Contact

# In [3]: Contact.objects.all()
# Out[3]: <QuerySet [<Contact: Contact object (3)>, <Contact: Contact object (6)>, <Contact: Contact object (7)>, <Contact: Contact object (8)>, <Contact: Contact object (9)>, <Contact: Contact object (10)>, <Contact: Contact object (11)>, <Contact: Contact object (12)>]>

# In [4]: Contact.objects.all()[0]
# Out[4]: <Contact: Contact object (3)>

# In [5]: Contact.objects.all()[0].name
# Out[5]: 'Utsav Parikh'

# In [6]: Contact.objects.all()[0].email
# Out[6]: 'utsavparikh00@gmail.com'


# In [10]: Contact.objects.filter(name="Utsav", phone="704310")
# Out[10]: <QuerySet []>

# In [11]: Contact.objects.filter(name="Utsav", phone="7043108606")
# Out[11]: <QuerySet []>

# In [12]: Contact.objects.filter(name="Utsav Parikh", phone="7043108606")
# Out[12]: <QuerySet [<Contact: Contact object (3)>]>

# In [13]: Contact.objects.all().first()
# Out[13]: <Contact: Contact object (3)>

# In [14]: Contact.objects.all().last()
# Out[14]: <Contact: Contact object (12)>

#admin.py ma model register karvu and setting ma jai ne installed app ma apps.py nu name copy kari ne muki devu..
# Create your views here....


from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

def index(request):
     context = {
          'variable':"this is sent",
          'variable1' : "this is sent 1"
     }
     # messages.success(request, 'Profile details updated.')
     return render(request, 'index.html',context)
     # return HttpResponse("<h1>This is My Own Home Page</h1>")

def about(request): 
     return render(request, 'about.html')
     # return HttpResponse("<h1>This is My Own About Page</h1>")
    
def service(request):
     return render(request, 'service.html')
     # return HttpResponse("<h1>This is My Own Service Page</h1>")


def contact(request):


     if request.method == "POST":
          name = request.POST.get('name')
          email = request.POST.get('email')
          phone = request.POST.get('phone')
          desc = request.POST.get('desc')
          contact = Contact(name=name, email=email, phone=phone, desc=desc, date= datetime.today())
          contact.save()
          messages.success(request, 'Your message has been Sent !!')
     return render(request, 'contact.html')
     # return HttpResponse("<h1>This is My Own Contact Page</h1>")
           
                                           