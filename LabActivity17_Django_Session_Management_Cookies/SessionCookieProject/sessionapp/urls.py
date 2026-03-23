from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('start/', views.start_session, name='start_session'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('clear-session/', views.clear_session, name='clear_session'),
    path('clear-cookies/', views.clear_cookies, name='clear_cookies'),
]
