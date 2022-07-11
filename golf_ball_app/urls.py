from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('balls/', views.golf_ball_index, name='index'),
    path('balls/<int:ball_id>/', views.golf_ball_detail, name='detail'),
    
]