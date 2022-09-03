from django.urls import path,include
from . import views

urlpatterns = [
    path('createop',views.createop,name="createop"),
    path('addtemperature',views.addtemperature,name="addtemperature"),
    path('give_prescriptions',views.prescriptions,name="prescriptions"),
    path('get_medicines',views.get_medicines,name="get_medicines"),
    path('update_price',views.update_price,name="update_price"),
    path('complete_payment/<str:email>',views.complete_payment,name="complete_payment"),
    path('book_appointment',views.book_appointment,name="book_appointment")
]