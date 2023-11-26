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

def action(request):
    return render(request, "products/movie_category/action.html")

def drama(request):
    return render(request, "products/movie_category/drama.html")

def experimental(request):
    return render(request, "products/movie_category/experimental.html")

def horror(request):
    return render(request, "products/movie_category/horror.html")

def romance(request):
    return render(request, "products/movie_category/romance.html")

def scifi(request):
    return render(request, "products/movie_category/sci_fi.html")

def series(request):
    return render(request, "products/movie_category/series.html")

def war(request):
    return render(request, "products/movie_category/war.html")