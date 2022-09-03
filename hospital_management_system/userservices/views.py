from django.http import HttpResponse,JsonResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from .models import opcard,medicines,bills, user_bills,medicines_list
from Accounts.models import Authentication
# Create your views here.
def createop(request):
    if request.user.is_authenticated and request.user.is_user:

        if request.method=="POST":
            patientname = request.POST["patientname"]
            patientmail = request.POST['patientmail']
            diseasename = request.POST['disease']
            if opcard.objects.filter(patientemail = patientmail).exists():
                messages.error(request,"OP card already issued please use it until it expires")
                return redirect("login")
            else:
                patient = Authentication.objects.get(username = patientmail)
                op = opcard.objects.create(patientname = patientname,patientemail=patient,disease = diseasename)
                op.save()
                messages.success(request,"Your op card issued successfully")
                return redirect("login")
    else:
        messages.error(request,"You are not authorized to access this please contact admin")
        return redirect("login")

def addtemperature(request):
    username  = request.GET['username']
    temp = request.GET['temperature']
    if opcard.objects.filter(patientemail=username).exists():
        op = opcard.objects.get(patientemail = username)
        op.temperature = temp
        op.save()
        return JsonResponse({
            'msg':"Temperature has been successfully added"
        })
    else:
        return JsonResponse({
            'msg':"User has not applied to op",
        })

def prescriptions(request):
    if request.user.is_authenticated and request.user.is_hospital:
        if request.method == "POST":
            username = request.POST['username']
            medicine_list = request.POST['medicines']
            medicine_list = medicine_list.strip()
            if medicine_list[-1] == ",":
                medicine_list = medicine_list[:len(medicine_list)-1]
            if Authentication.objects.filter(username = username).exists():
                user = Authentication.objects.get(username=username)
                new_med_list = medicines_list.objects.create(patientemail = user,medicine_list = medicine_list)
                new_med_list.save()
                medicine_list = medicine_list.split(",")
                for medicine in medicine_list:
                    medicine = medicine.strip()
                    medicine = medicine.split(" ")
                    if len(medicine) == 1:
                        medicine.append(0)
                    if medicines.objects.filter(patientemail = user,medicine_name = medicine[0]).exists():
                        new_med = medicines.objects.get(patientemail  = user,medicine_name = medicine[0])
                        new_med.medicine_quantity = medicine[1]
                        new_med.is_settled = False
                        new_med.price = 0.0
                        new_med.save()
                    else:
                        med = medicines.objects.create(patientemail = user,medicine_name=medicine[0],medicine_quantity = medicine[1])
                        med.save()
                op = opcard.objects.get(patientemail = user)
                op.is_assigned = True
                op.is_appointed = False
                op.save()
                if bills.objects.filter(patientemail = user).exists():
                    hf = bills.objects.get(patientemail = user)
                    hf.medicines_provided = False
                    hf.save()
                else:
                    hf = bills.objects.create(patientemail = user,medicines_provided = False)
                    hf.save()
                return redirect('login')
            else:
                messages.error(request,"User doesn't exist please contact Admin")
                return redirect("login")
    else:
        messages.error(request,"You are not authorized to access this please contact Admin")
        return redirect("login")

def get_medicines(request):
    if request.user.is_authenticated and request.user.is_medical:
        if request.method == "POST":
            username = request.POST['user_mail']
            if medicines.objects.filter(patientemail = username).exists():
                if Authentication.objects.filter(username=username).exists():
                    user_table = Authentication.objects.get(username = username)
                    bill = bills.objects.get(patientemail = username,bill_status = False)
                    name = user_table.first_name+" "+user_table.last_name
                    email = user_table.username
                    connum = user_table.Contact_number
                    gender = user_table.Gender
                    age = user_table.Age
                    total_price = bill.total_amount
                    medicine_list = medicines.objects.filter(patientemail=username,is_settled = False)
                    return render(request,'show_medicines.html',{
                        'medicines':medicine_list,
                        'name':name,
                        'contact':connum,
                        'gender':gender,
                        'age':age,
                        'email':email,
                        'total_price':total_price
                    })
                else:
                    name="User doesn't exists"
                    connum = None
                    gender = None
                    age = None
                    email=None
                    total_price = None
                    medicine_list = medicines.objects.filter(patientemail = username,is_settled = False)
                    return render(request,'show_medicines.html',{
                        'medicines':medicine_list,
                        'name':name,
                        'contact':connum,
                        'gender':gender,
                        'age':age,
                        'email':email
                    })
            else:
                messages.error(request,"User doesn't have any medicines to proovide")
                return redirect("login")
    else:
        messages.error(request,'You are not authorized to access this please contact Admin')

def update_price(request):
    if request.user.is_authenticated and request.user.is_medical:

        if request.method == "GET":
            username = request.GET['username']
            medname = request.GET['medname']
            price = request.GET['price']
            if medicines.objects.filter(patientemail = username,medicine_name = medname).exists():
                med = medicines.objects.get(patientemail = username,medicine_name = medname)
                med.price = price
                med.save()
                total_price = 0
                medicine_list = medicines.objects.filter(patientemail = username,is_settled = False)
                for medicine in medicine_list:
                    total_price+=float(medicine.price)
                bill = bills.objects.get(patientemail = username)
                bill.total_amount = total_price
                bill.save()
                return JsonResponse({
                    'error':False,
                })
            else:
                return JsonResponse({
                    'error':True,
                    'msg':username + " has no medicines with name "+medname
                })
    else:
        return JsonResponse({
            'error':True,
            'msg':"You are not authorized to access this please antact Admin"
        })

def complete_payment(request,email):
    if request.user.is_authenticated and request.user.is_medical:
        if Authentication.objects.filter(username = email).exists():
            user = Authentication.objects.get(username = email)
            if bills.objects.filter(patientemail = email).exists():
                bill = bills.objects.get(patientemail = email)
                ubills = user_bills.objects.create(patientemail = user,bill_status=True,total_amount = bill.total_amount)
                ubills.save()
                bill.medicines_provided = True
                bill.total_amount = 0.0
                bill.save()
                meds = medicines.objects.filter(patientemail = user)
                for med in meds:
                    med.is_settled = True
                    med.save()
                return redirect("login")
            else:
                messages.error(request,"User "+email+" has no medicines assigned please try again")
                return redirect("login")
        else:
            messages.error(request,"User doesn't exists please contact Admin")
            return redirect("login")
    else:
        messages.error(request,"You are not authorized to access this please contact Admin")
        return redirect("login")

def book_appointment(request):
    if request.user.is_authenticated and request.method == "POST":
        username = request.user
        disease = request.POST['disease']
        op = opcard.objects.get(patientemail = username)
        op.is_assigned  = False
        op.is_appointed = True
        op.disease = disease
        op.save()
        messages.success(request,"Your apointment has been updated , please visit the hospital for health check ")
        return redirect('login')
    else:
        messages.error(request,'please login to continue')
        return redirect("login")