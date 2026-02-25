from django.shortcuts import render
from .models import Slide

def carousel_view(request):
    slides = Slide.objects.filter(is_active=True).order_by("order", "id")
    return render(request, "carousel/carousel.html", {"slides": slides})
