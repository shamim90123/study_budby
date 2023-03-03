from django.shortcuts import render
from django.http import HttpResponse
from .models import Room

rooms = [
	{'id': 1, 'name': 'Let learn the python!'},
	{'id': 2, 'name': 'Let learn the PHP!'},
	{'id': 3, 'name': 'Let learn the JAVA!'},
	{'id': 4, 'name': 'Let learn the JS!'}
]


def home(request):
	rooms = Room.objects.all()
	context = {'rooms': rooms}
	return render(request, 'base/home.html', context)


def room(request, pk):
	# room = None
	# for i in rooms:
	# 	if i['id'] == int(pk):
	# 		room = i
	room = Room.objects.get(id=pk)
	context = {'room': room}
	return render(request, 'base/room.html', context)


def createRoom(request):
	context = {}
	return render(request, 'base/room_form.html', context)