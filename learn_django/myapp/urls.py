from django.urls import path

from . import views

urlpatterns = [
    # path('hello/', views.hello, name='hello'),
    # path('shubhi/', views.shubhi, name='shubhi'),
    # path('ashu/', views.shubhi, name='ashu')
    path('shubhi/', views.ShubhiPageView.as_view(), name='shubhi'),
    path('ashu/', views.AshuPageView.as_view(), name='ashu'),






]
