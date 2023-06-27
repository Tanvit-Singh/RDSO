from django.db import models
from django.contrib.auth import get_user_model

User=get_user_model()

# Create your models here.

class profile(models.Model):
    username=models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.TextField()
    last_name=models.TextField()
    location=models.CharField(max_length=100, blank=True)
    age=models.IntegerField()
    bio=models.TextField(blank=True)

    def __str__(self):
        return self.user.username

class Contact(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=12)
    desc=models.TextField()
    date=models.DateField()
    
class mainmenu(models.Model):
    ROLES = (
        ('admin', 'Admin'),
        ('supervisor', 'Supervisor'),
        ('dataentry', 'Data Entry'),
    )

    menucode = models.IntegerField()
    menuname = models.CharField(max_length=100)
    menutype = models.IntegerField()
    role = models.CharField(max_length=20, choices=ROLES,default='admin')

class MenuList(models.Model):
    Menucode= models.IntegerField()
    MenuType=models.IntegerField()
    menuname = models.CharField(max_length=100)
    submenuname = models.CharField(max_length=100)
    menulink = models.CharField(max_length=100)
    mainmenu=models.ForeignKey(mainmenu, on_delete=models.CASCADE,default=1)
 
    def __str__(self):
        return self.menuname
     
    menulist_objects = models.Manager()