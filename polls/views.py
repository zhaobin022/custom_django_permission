from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import json,datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import django.utils.timezone
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render_to_response
import StringIO
import SocketServer
import logging
logger = logging.getLogger('web_apps')
import utils
# Create your views here.



def login(request):
    print request.POST
    print request.GET
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect('/')
        else:
            return render_to_response('login.html')
    else:
        return render_to_response('login.html')

@login_required
def index(request):
    return render_to_response('index.html')

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/login/')


@utils.token_required
def test(request):
    return render_to_response('index.html')
