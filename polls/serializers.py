__author__ = 'zhaobin022'
from rest_framework import serializers
from polls import models

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.UserProfile
        fields = ('url', 'username')



class ServerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Server
        fields = ('url', 'server_name','ip')
