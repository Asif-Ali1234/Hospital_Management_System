import random as r
import time

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.models import auth
from django.core.mail import send_mail
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_protect, ensure_csrf_cookie

from userservices.models import bills, opcard, user_bills,medicines_list

from .models import Authentication

# Create your views here.

otpdict={}

registerotpdict = {}

attemptsdict={}

adminmail = settings.EMAIL_HOST_USER

def dashboard(request):
    if request.user.is_authenticated:
        usertype = Authentication.objects.get(username=request.user)
        if usertype.is_user:
            bill_list = user_bills.objects.filter(patientemail = usertype.username)
            med_list = medicines_list.objects.filter(patientemail = usertype.username)
            if opcard.objects.filter(patientemail = usertype.username).exists():
                return render(request,'User_dashboard.html',{
                    'opissued':True,
                    'opcontent':opcard.objects.get(patientemail = usertype.username).enddate,
                    'appointment':opcard.objects.get(patientemail = usertype.username).is_appointed,
                    'disease_name':opcard.objects.get(patientemail = usertype.username).disease,
                    'bills':bill_list,
                    'medicines':med_list,
                })
            else:
                return render(request,"User_dashboard.html",{
                    'opissued':False,
                    'bills':bill_list,
                    'medicines':med_list,
                })
        elif usertype.is_hospital:
            patient_list = opcard.objects.filter(is_assigned = False)
            return render(request,"Hospital_dashboard.html",{
                'patients':patient_list,
            })
        elif usertype.is_medical:
            patient_list = bills.objects.filter(medicines_provided = False).select_related("patientemail")
            return render(request,"Medicine_dashboard.html",{
                'patients':patient_list,
            })
    
    else:
        messages.error(request,'you are  not authenticated please login again')
        return redirect('login')

def register(request):
    if request.method=="POST":
        first_name=request.POST["first_name"]
        gender=request.POST["radio_input"]
        number=request.POST["phn_number"]
        username=request.POST["E-mail"]
        passwd=request.POST["passwd"]
        age = request.POST["age"]
        confirmedpassword=request.POST["confirmpassword"]
        if Authentication.objects.filter(username=username).exists():
            messages.error(request,"Username Already Registered")
            return redirect("register")
        elif passwd!=confirmedpassword:
            messages.warning(request,"Passwords Not Matched Please Try again")
            return redirect("register")
        else:
            user=Authentication.objects.create_user(username=username,password=passwd,first_name=first_name,
            Contact_number=number,Gender=gender,Age = age,email= username , is_user = True)
            user.save()
            messages.success(request,"You have been successfully registered with us")
            return redirect("login")
    else:
        return render(request,"User_Registration_form.html")

@ensure_csrf_cookie
@csrf_protect
def login(request):
    if request.user.is_authenticated:
        return redirect('profile')
    if request.method=="POST":
        username=request.POST["username"]
        passwd=request.POST["passwd"]

        user=auth.authenticate(username=username,password=passwd)
        if Authentication.objects.filter(username=username).exists():

            if user is not None:
                auth.login(request,user)
                return redirect('profile')
            else:
                messages.error(request,"Username and Password is not matched")
                return redirect("login")
        else:
            messages.warning(request,"Sorry We Couldn't find you ....Connect with us first")
            return redirect('login')
    else:
        return render(request,"login.html")

def logout(request):
    auth.logout(request)
    messages.info(request,"You have been logged out Successfully")
    return redirect("/")

def forgotpassword(request):
    if(request.method=="POST"):
        otp=""
        for i in range(6):
            otp+=str(r.randint(1,9))
        receiver=request.POST["receiver_name"]
        if Authentication.objects.filter(username=receiver).exists():
            userdetails=Authentication.objects.get(username=receiver)
            firstname=userdetails.first_name
            send_mail('[Hospital Name]Please Reset Your Password','Hello '+ str(firstname) +' , Warm Regards \n'+'\nIt seems you have forgotten your Account Password\n'+'\nBut don\'t worry You can Reset your Password  Using OTP below :\n'+'\n\t\t\t\t\tYour Otp to reset password is '+str(otp)+'\n\n\n\nThanks,\nThe Hospital Management',adminmail,
            [receiver,],fail_silently=False)
            otpdict[receiver]=otp
            attemptsdict[receiver]=3
            messages.info(request,"OTP has been sent to your registered Email Id or Username")
            return render(request,"otp_verification.html",{'name':receiver})
        else:
            messages.error(request,"Username doesn't exist.Please Enter Valid Username")
            return redirect("forgotpassword")
    else:
        return render(request,'forgotpassword.html')

def verifyotp(request):
    if(request.method=="POST"):
        user_otp=request.POST["user_otp"]
        receiver=request.POST["receiver"]
        try:
            otp=otpdict[receiver]
            if attemptsdict[receiver]>0:

                if(otp==user_otp):
                    del(otpdict[receiver])
                    attemptsdict[receiver]=0
                    return render(request,"change_passwd.html",{'name':receiver})
                else:
                    messages.error(request,"Otp is not matched Please Try Again")
                    atemptstr="Remaining Attempts : "+str(attemptsdict[receiver])
                    attemptsdict[receiver]-=1
                    return render(request,"otp_verification.html",{'name':receiver,'attempts':atemptstr})
            elif attemptsdict[receiver]==0:
                messages.error(request,"Otp Attempts limit reached . Please Generate Again")
                return redirect("forgotpassword")
        except KeyError:
            messages.error(request,"The otp generated has expired or deleted Please regenerate again")
            return redirect("forgotpassword")
    else:
        return render(request,"otp_verification.html")

def changepassword(request):
    if(request.method=="POST"):
        requested_user=request.POST["change_requested_user"]
        passwd=request.POST["npasswd"]
        cnfrmpasswd=request.POST["cnfrmpasswd"]
        if passwd==cnfrmpasswd:
            user=Authentication.objects.get(username=requested_user)
            user.set_password(passwd)
            user.save()
            auth.logout(request)
            firstname=user.first_name
            send_mail('[Hosspital Name]Password Changed','Hello '+str(firstname)+' , Security Threat \n'+'\nYour password for the the account '+str(requested_user[:3])+'*'*int(len(str(requested_user)))+str(requested_user[::-1][:3][::-1]) +' has changed recently \n'+'\nIf you don\'t change your password contact us Immediately with your details'+'\n\n If this was you simply ignore this email '+'\n\n\n\nThanks,\nThe Hospital Management',adminmail,
            [requested_user,],fail_silently=False)
            messages.success(request,"Your password has been successfully changed Please login again")
            return redirect("login")
        else:
            messages.warning(request,"Passwords Not Matched")
            return render(request,"change_passwd.html",{'name':requested_user})
    else:
        return render(request,"change_passwd.html")

def changepasswordafterlogin(request):
    if request.method == "POST":
        curpasswd=request.POST["oldpasswd"]
        username=request.user
        userauth=auth.authenticate(username=username,password=curpasswd)
        if userauth is None:
            messages.error(request,"Current Password not matched Please try again or reset it by signing out")
            return redirect('changepasswordafterlogin')
        else:
            passwd=request.POST["newpasswd"]
            cnfrmpasswd=request.POST["cnfrmpasswd"]
            if passwd==cnfrmpasswd:
                user=Authentication.objects.get(username=username)
                user.set_password(passwd)
                user.save()
                auth.logout(request)
                firstname=user.first_name
                send_mail('[Hospital Name]Password Changed','Hello '+str(firstname)+' , Security Threat \n'+'\nYour password for the the account '+str(username)+' has changed recently \n'+'\nIf you don\'t change your password contact us Immediately with your details'+'\n\n If this was you simply ignore this email '+'\n\n\n\nThanks,\nThe Hospital Management',adminmail,
                [username,],fail_silently=False)
                messages.success(request,"Your password has been successfully changed Please login again")
                return redirect("login")
            else:
                messages.error(request,"Passwords not matched Please try again")
                return redirect('changepasswordafterlogin')
    else:
        return render(request,'chngpasswdaftrlgn.html')

def deleteaccount(request):
    if request.method=="POST":
        username=request.user

        userpasswd=request.POST['reqpasswd']

        userauth=auth.authenticate(username=username,password=userpasswd)

        if userauth is None:
            messages.error(request,'Password not matched with your account')

            return render(request,'deleteaccount.html',{'username':username})

        else:
            auth.logout(request)

            user=Authentication.objects.get(username=username)

            deletedtuple=user.delete()

            totalsavings=deletedtuple[0]

            messages.warning(request,'we have deleted '+str(totalsavings)+' fields of you , If you face any problems feel free to contact us')
            return redirect("/")


    else:
        return render(request,'deleteaccount.html',{'username':request.user})

def checkusername(request):
    username = request.GET['username']

    if Authentication.objects.filter(username=username).exists():
            time.sleep(2)
            data = {
                'error':True,
                'msg':'Username already exists Please try again',
            }
            return JsonResponse(data)
    
    else:
        otp=""
        for i in range(6):
            otp+=str(r.randint(1,9))
        time.sleep(1)
        send_mail('[Hospital Name]Verify Email','Please give the below OTP in order to verify your account registered with Hospital Name'+'\nOTP is '+str(otp)+'\n\n\n\nThanks,\nThe Hospital Management',adminmail,
                [username,],fail_silently=False)
        registerotpdict[username] = otp

        data = {
            'error':False,
            'msg':'OTP has been sent to your mail',
        }

        return JsonResponse(data)

def verifyregistrationotp(request):
    otp = request.GET['registerotp']

    username = request.GET['username']

    if username in registerotpdict.keys():
        time.sleep(2)
        if registerotpdict[username] == otp:
            data = {
                'error':False,
            }
            del(registerotpdict[username])
        else:
            data = {
                'error':True,
                'msg':'OTP is not matched or Invalid Please try again'
            }
    else:
        time.sleep(1)
        data = {
            'error':True,
            'msg':'OTP is not generated for this mail Please generate again'
        }

    return JsonResponse(data)

def checkloginusername(request):
    username = request.GET['username']

    time.sleep(1)

    if Authentication.objects.filter(username=username).exists():
        data = {
            'error':False
        }
    else:
        data = {
            'error':True,
            'msg':"Username doesn't exists please try again"
        }

    return JsonResponse(data)
