from django.db import models

# Create your models here. (for tables)
# "Models field django" Google it

class Contact(models.Model):
    class Meta:
        db_table = 'contact'
    name  = models.CharField(max_length=50)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length= 13, null= True, blank= True)
    desc  = models.TextField()
    date  = models.DateField()

# Register model "admin.py" > from home.models import Contact
    
    # To get entries in admin by the # name # of the person

    def __str__(self):
        return self.name
