# chat/urls.py
from django.urls import path
from . import views  # Import the views for the 'chat' app

urlpatterns = [
    # The home page will render the home view.
    path('', views.home, name='home'),
    
    path('login/', views.user_login, name='login'),
       # Room view that accepts a room name as a dynamic URL parameter.
    path('room/<str:room_name>/', views.room, name='room'),
    
    # Additional URLs for register, login, logout (already defined in project urls.py)
    path('register/', views.register, name='register'),
    path('logout/', views.user_logout, name='logout'),
]
