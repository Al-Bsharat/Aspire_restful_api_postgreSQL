from django.urls import path
from profiles_api import views

urlpatterns = [
    path('images/', views.ImageApiView.as_view())
]
