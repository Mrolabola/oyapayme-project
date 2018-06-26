from rest_framework import viewsets, permissions

from .serializers import AdminSerializer, AgentSerializer
from ..models import Admin, Agent, User


class AdminViewset(viewsets.ModelViewSet):
    """
    This endpoint provides list, detail, create, retrieve and delete action for an admin
    """

    queryset = Admin.objects.all()
    serializer_class = AdminSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class AgentViewset(viewsets.ModelViewSet):
    """
    This endpoint provides list, detail, create, retrieve and delete action for an agent
    """

    queryset = Agent.objects.all()
    serializer_class = AgentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
