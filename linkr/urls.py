from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', lambda request: redirect('home')),  # Redirect root to home view
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),  # This includes login, logout, etc.
    path('tracker/', include('tracker.urls')),
]

# Optional: Configure logout redirect
from django.conf import settings
settings.LOGOUT_REDIRECT_URL = 'home'  # Redirect to home page after logout
