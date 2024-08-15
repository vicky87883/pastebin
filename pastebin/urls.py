from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_snippet, name='home'),  # Redirect root URL to create_snippet
    path('create/', views.create_snippet, name='create_snippet'),
    path('snippet/<str:unique_url>/', views.view_snippet, name='view_snippet'),
]
