from django.shortcuts import render

# Create your views here.
def alope_home(request):
    return render(request, 'index.html')