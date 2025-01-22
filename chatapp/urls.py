# chatapp/urls.py
from django.contrib import admin
from django.urls import path, include  # include is used to include app URLs
from chat import views  # Import views from the 'chat' app

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin page URL
    path('accounts/', include('django.contrib.auth.urls')),  # Django's default authentication URLs
    path('', views.home, name='home'),  # Home URL
    path('login/', views.user_login, name='login'),  # Login URL
    path('room/<str:room_name>/', views.room, name='room'),  # Chat room URL
    path('register/', views.register, name='register'),  # Registration URL
    path('logout/', views.user_logout, name='logout'),  # Logout URL
]
