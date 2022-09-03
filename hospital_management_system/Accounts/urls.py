from django.urls import path,include
from . import views
urlpatterns=[
    path('register',views.register,name="register"),
    #path('ContactUs',views.ContactUs,name="ContactUs"),
    path('login',views.login,name="login"),
    path('logout',views.logout,name="logout"),
    path('forgotpassword',views.forgotpassword,name="forgotpassword"),
    path('changepassword',views.changepassword,name="changepassword"),
    path('verifyotp',views.verifyotp,name="verifyotp"),
    path('changepasswordafterlogin',views.changepasswordafterlogin,name="changepasswordafterlogin"),
    path('deleteaccount',views.deleteaccount,name="deleteaccount"),
    path('checkusername',views.checkusername,name="checkusername"),
    path('verifyregistrationotp',views.verifyregistrationotp,name="verifyregistrationotp"),
    path('checkloginusername',views.checkloginusername,name="checkloginusername"),
    path('dashboard',views.dashboard,name="profile"),
]