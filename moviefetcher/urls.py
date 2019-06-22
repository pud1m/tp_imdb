from django.urls import include, path
from . import views

app_name = 'moviefetcher'
urlpatterns = [
    path('teste/', views.teste, name='teste'),
    path('requester/', views.requester, name='requester'),
    path('pedido/', views.pedido, name='pedido'),
    ]