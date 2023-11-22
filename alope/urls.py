
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('alopehomeapp.urls')),
    path('movies/', include('movies.urls')),
    path('music/', include('music.urls')),
    path('sports/', include('sports.urls')),
    path('news/', include('news.urls')),
]
