
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('132c9569-000a-4e54-8ce3-7d22c9371072.html',views.verify,),
]
