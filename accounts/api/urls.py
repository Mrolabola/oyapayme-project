from django.urls import path, include

from rest_framework.routers import DefaultRouter


from . import viewsets

router = DefaultRouter()
router.register(r'admins', viewsets.AdminViewset)
router.register(r'agents', viewsets.AgentViewset)

urlpatterns = [
    path('', include(router.urls)),
]

