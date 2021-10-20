from django.shortcuts import render
from . import models


# Create your views here.
def all_rooms(request):
    rooms = models.Room.objects.all()
    return render(request, "all_rooms.html", context={"rooms": rooms})
