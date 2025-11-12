from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProfileView, ProjectViewSet

router = DefaultRouter()
router.register(r'projects', ProjectViewSet, basename='project')

urlpatterns = [
    path('profile/', ProfileView.as_view(), name='profile'),
    path('', include(router.urls)),
]
