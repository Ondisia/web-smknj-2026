from django.shortcuts import render

# Create your views here.
def beranda(request):
    return render(request, 'index.html')

def profil(request):
    return render(request, 'profil_sekolah.html')