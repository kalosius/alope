from django.shortcuts import render, redirect
from . forms import MemberForm
from . models import Member
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
# Create your views here.

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('alope_home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {"form":form})


def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('alope_home')
        
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {"form":form})

def alope_home(request):
    all_members = Member.objects.all()
    return render(request, 'index.html', {'all':all_members})

def join(request):
    if request.method == "POST":
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/join")
        
        else:    
            return render(request, 'join.html')
        

import requests

def get_movie_details(api_key, movie_id):
    base_url = "https://api.themoviedb.org/3/movie/"
    endpoint = f"{movie_id}?api_key={api_key}"

    # Make the API request
    response = requests.get(base_url + endpoint)
    
    if response.status_code == 200:
        # Parse and print the movie details
        movie_details = response.json()
        print("Title:", movie_details["title"])
        print("Overview:", movie_details["overview"])
        print("Release Date:", movie_details["release_date"])
        print("Average Vote:", movie_details["vote_average"])
        print(response.text)
    else:
        print("Error:", response.status_code)

# Replace 'YOUR_API_KEY' with your actual TMDb API key
api_key = '6de0ba4758d5f04b2c2e9dd6ec77396c'
movie_id = 550  # Example movie ID (Inception)

get_movie_details(api_key, movie_id)

# myapp/views.py
from django.shortcuts import render
import requests

def movie_details(request, movie_id):
    api_key = '6de0ba4758d5f04b2c2e9dd6ec77396c'
    base_url = "https://api.themoviedb.org/3/movie/"
    endpoint = f"{movie_id}?api_key={api_key}"

    # Make the API request
    response = requests.get(base_url + endpoint)
    
    if response.status_code == 200:
        # Parse the movie details
        movie_details = response.json()

        # Render the template with movie details
        return render(request, 'index.html', {'movie_details': movie_details})
    else:
        return render(request, 'index.html', {'status_code': response.status_code})




def get_movie_details(api_key, movie_id):
    base_url = "https://api.themoviedb.org/3/movie/"
    endpoint = f"{movie_id}?api_key={api_key}"

    # Make the API request
    response = requests.get(base_url + endpoint)
    
    if response.status_code == 200:
        # Parse and return the movie details
        return response.json()
    else:
        return {'error': response.status_code}