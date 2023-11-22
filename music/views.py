from django.shortcuts import render

# Create your views here.
def songs(request):
    return render(request, 'products/music.html')