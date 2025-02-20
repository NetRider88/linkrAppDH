# tracker/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('generate/', views.generate_link, name='generate_link'),
    path('analytics/<str:short_id>/', views.analytics, name='analytics'),
    path('analytics/<str:short_id>/export/', views.export_analytics, name='export_analytics'),
    path('delete/<str:short_id>/', views.delete_link, name='delete_link'),
    path('profile/', views.profile, name='profile'),
    path('campaign/new/', views.create_campaign, name='create_campaign'),
    path('campaign/<int:campaign_id>/', views.campaign_detail, name='campaign_detail'),
    path('campaign/<int:campaign_id>/delete/', views.delete_campaign, name='delete_campaign'),
    path('<str:short_id>/', views.track_click, name='track_click'),
]
