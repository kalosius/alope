from django.shortcuts import render

# Create your views here.
def home_movie(request):
    return render(request, 'products/home_movie.html')