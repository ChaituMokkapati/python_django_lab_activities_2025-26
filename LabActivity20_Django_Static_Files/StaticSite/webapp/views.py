from django.shortcuts import render


def home(request):
    return render(request, 'webapp/home.html')

# Create your views here.
