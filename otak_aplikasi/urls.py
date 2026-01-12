from django.urls import path
from . import views

urlpatterns = [
   path('', views.beranda, name='home'),
   path('profil-sekolah/', views.profil, name='profile'),
]

