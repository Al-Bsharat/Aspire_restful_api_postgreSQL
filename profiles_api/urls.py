from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles_api import views

router = DefaultRouter()
router.register('images-view-set', views.ImageViewSet, base_name='images-view-set')

urlpatterns = [
    path('images/', views.ImageApiView.as_view()),
    path('', include(router.urls))
]
