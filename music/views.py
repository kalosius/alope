from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . models import *
# Create your views here.

class SongApiView(APIView):
    def get(self, request):
        all_songs = Pop.objects.all().values()
        return Response({"Message":"List of Songs","Song List":all_songs})
    
    def post(self, request):

        Pop.objects.create(id=request.data["id"], 
                           title=request.data["title"], 
                           artist=request.data["artist"],)

        song = Pop.objects.all().filter(id=request.data["id"]).values()
        return Response({"Message":"New Song Added!","Song":song})


def songs(request):

    return render(request, 'products/music.html')