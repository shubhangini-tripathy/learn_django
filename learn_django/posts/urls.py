from django.urls import path

from . import views

urlpatterns = [
    path('a/', views.HomePageView.as_view(), name='home'),
]