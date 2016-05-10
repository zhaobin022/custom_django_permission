__author__ = 'zhaobin022'
from rest_framework import viewsets
from polls.serializers import UserSerializer,ServerSerializer
from polls.models import UserProfile,Server

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer


class ServerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Server.objects.all()
    serializer_class = ServerSerializer


