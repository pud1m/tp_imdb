from django.urls import include, path
from . import views

app_name = 'moviefetcher'
urlpatterns = [
    path('teste/', views.teste, name='teste'),
    ]