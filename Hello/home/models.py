from django.db import models

# Create your models here.
#aapda database ne define kare che..
#contact ek table che aapdu....

#makemigration: Create changes and store in a file
#migrate: apply the pending changes created by makemigrates
class Contact(models.Model):
     name  =  models.CharField(max_length=122)
     email =  models.CharField(max_length=122)
     phone =  models.CharField(max_length=12)
     desc  =  models.TextField(null=True)
     date  =  models.DateField()

def __str__(self):
    return self.name

