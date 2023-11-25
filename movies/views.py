from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . models import *
from . serializers import *
# Create your views here.

class MovieApiView(APIView):
    serializer_class = MovieSerializer
    def get(self, request):
        all_movies = Movie.objects.all().values()
        return Response({"Message":"List of Movies","Movies List":all_movies})

    
    def post(self, request):
        print('Request data is : ', request.data)
        serializer_obj = MovieSerializer(data=request.data)

        if (serializer_obj.is_valid()):

            Movie.objects.create(id=serializer_obj.data.get("id"), 
                            title=serializer_obj.data.get("title"), 
                            description=serializer_obj.data.get("description"),)

        movie = Movie.objects.all().filter(id=request.data["id"]).values()
        return Response({"Message":"New Movie Added!","Movie":movie})

def home_movie(request):
    return render(request, 'products/home_movie.html')