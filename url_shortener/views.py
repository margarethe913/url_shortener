from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.http import HttpResponse
import urllib3
from django.views.decorators.csrf import csrf_exempt
import uuid
import pymongo
from pymongo import MongoClient
import os, json
from django.shortcuts import render
from django.views.generic import TemplateView # Import TemplateView

# Add the two views we have been talking about  all this time :)
class HomePageView(TemplateView):
    template_name = "index.html"


class ResultPageView(TemplateView):
    template_name = "result.html"

def index(request):
    request.COOKIES['key'] = str(uuid.uuid1())
    response = render(request, 'index.html')
    response.set_cookie('key', str(uuid.uuid1()))
    return response
