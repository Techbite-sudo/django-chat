from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path("<str:roomname>/",views.room, name="roomname"),
    path("checkview",views.checkview, name="checkview"),
    path("send",views.send,name="send"),
    
]

