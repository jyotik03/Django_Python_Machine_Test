# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClientViewSet, ProjectViewSet

router = DefaultRouter()
router.register(r'clients', ClientViewSet, basename='client')
router.register(r'projects', ProjectViewSet, basename='project')

urlpatterns = [
    path('', include(router.urls)),
    path('clients/<int:pk>/projects/', ProjectViewSet.as_view({'post': 'add_project'})),
    path('projects/assigned/', ProjectViewSet.as_view({'get': 'assigned_projects'})),
]
