__author__ = 'zhaobin022'
from rest_framework import viewsets
from polls.serializers import UserSerializer,ServerSerializer
from polls.models import UserProfile,Server
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.contrib.auth.decorators import login_required
from rest_framework.authtoken.models import Token
import json
import utils

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



class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
@utils.token_required
def server_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        servers = Server.objects.all()
        serializer = ServerSerializer(servers, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ServerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

# @utils.token_required
# def obtain_auth_token(request):
#     if request.method == 'POST':
#         print 'in post'
#         token = Token.objects.get_or_create(user=request.user)
#         return HttpResponse(json.dumps(token))
