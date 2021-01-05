from django.urls import path

from . import views



urlpatterns = [
    path('', views.home, name='home'), 
    path('info/', views.info, name='info'), 
    path('result/', views.result, name='result'),
    path('result/plots/', views.plots, name = 'plots'), 
    path('result/histograms', views.histo, name= 'histograms'),  
]
