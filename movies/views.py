from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . models import *
from . serializers import *
import requests
# Create your views here.

# This is the API for all the movies
import requests

def get_movie_info(movie_title):
    api_key = 'cb31935fc07792f615d11de334081eb4'
    api_endpoint = 'https://api.themoviedb.org/3/movie/550?api_key=cb31935fc07792f615d11de334081eb4'
    params = {
        'api_key': api_key,
        'title': movie_title,
    }

    try:
        # Make the API request
        response = requests.get(api_endpoint, params=params)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse and return the response data (consider using JSON parsing for APIs that return JSON)
            return response.json()
        else:
            # Print an error message if the request was not successful
            print(f"Error: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Example usage
movie_title = 'Inception'
result = get_movie_info(movie_title)
print(result)





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
                            movie_name=serializer_obj.data.get("movie_name"), 
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