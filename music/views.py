from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . models import *
from . serializers import *
# Create your views here.

class SongApiView(APIView):
    serializer_class = PopSerializer
    def get(self, request):
        all_songs = Music.objects.all().values()
        return Response({"Message":"List of Songs","Song List":all_songs})

    
    def post(self, request):
        print('Request data is : ', request.data)
        serializer_obj = PopSerializer(data=request.data)

        if (serializer_obj.is_valid()):

            Music.objects.create(id=serializer_obj.data.get("id"), 
                            title=serializer_obj.data.get("title"), 
                            artist=serializer_obj.data.get("artist"),)

        song = Music.objects.all().filter(id=request.data["id"]).values()
        return Response({"Message":"New Song Added!","Song":song})


def songs(request):
    return render(request, 'products/music.html')

def country(request):
    return render(request, 'products/songs/country.html')

def gospel(request):
    return render(request, 'products/songs/gospel.html')

def hiphop(request):
    return render(request, 'products/songs/hip_hop.html')

def jazz(request):
    return render(request, 'products/songs/jazz.html')

def pop(request):
    return render(request, 'products/songs/pop.html')

def rnb(request):
    return render(request, 'products/songs/rnb.html')

def rock(request):
    return render(request, 'products/songs/rock.html')

def reggae(request):
    return render(request, "products/songs/reggae.html")

def electronic(request):
    return render(request, "products/songs/electronic.html")