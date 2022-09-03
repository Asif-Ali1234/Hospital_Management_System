from django.db import models
from Accounts.models import Authentication 
from datetime import datetime,timedelta

# Create your models here.
def get_enddate():
    return datetime.today() + timedelta(days=30)

class opcard(models.Model):
    patientname = models.CharField(max_length=100)
    patientemail = models.OneToOneField(Authentication,on_delete=models.CASCADE,unique=True,null=False)
    startdate = models.DateField(auto_now_add=True)
    enddate = models.DateField(default=get_enddate)
    disease = models.CharField(max_length = 100)
    temperature = models.FloatField(default=0)
    is_assigned = models.BooleanField(default=False)
    is_appointed = models.BooleanField(default = False)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.patientemail)

class medicines_list(models.Model):
    patientemail = models.ForeignKey(Authentication,on_delete = models.CASCADE,null=False)
    medicine_list = models.CharField(max_length = 1024)
    date_assigned = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.patientemail)

class medicines(models.Model):
    patientemail = models.ForeignKey(Authentication,on_delete=models.CASCADE,null = False)
    medicine_name = models.CharField(max_length = 30)
    medicine_quantity = models.IntegerField()
    price = models.FloatField(default=0.0)
    is_settled = models.BooleanField(default = False)

class bills(models.Model):
    patientemail = models.OneToOneField(Authentication,on_delete=models.CASCADE,primary_key=True)
    medicines_provided = models.BooleanField(default = False)
    bill_status = models.BooleanField(default = False)
    total_amount = models.FloatField(default = 0.0)
    date_requested = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.patientemail)

class user_bills(models.Model):
    patientemail = models.ForeignKey(Authentication,on_delete=models.CASCADE)
    bill_status = models.BooleanField(default = False)
    total_amount = models.FloatField(default = 0.0 )
    date_generated = models.DateTimeField(auto_now_add = True)
