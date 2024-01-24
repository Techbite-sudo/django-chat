from django.shortcuts import render, redirect
from chat.models import Room, Message
from django.http import HttpResponse, JsonResponse


# Create your views here.
def home(request):
    return render(request, "home.html")


def room(request, roomname):
    username = request.GET.get("username")
    room_details = Room.objects.get(name=roomname)
    return render(request,"room.html",{
        "username": username,
        "room_details": room_details,
        "roomname": roomname
    })


def checkview(request):
    roomname = request.POST["room_name"]
    username = request.POST["username"]
    if Room.objects.filter(name=roomname).exists():
        return redirect("/" + roomname + "/?username=" + username)
    else:
        newroom = Room.objects.create(name=roomname)
        newroom.save()
        return redirect("/" + roomname + "/?username=" + username)
    
    
def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']
    
    newmessage = Message.objects.create(value=message, user=username, room=room_id)
    newmessage.save()
    return HttpResponse("Message sent successfully")

    
