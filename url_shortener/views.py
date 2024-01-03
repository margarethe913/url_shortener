from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.http import HttpResponse
import urllib3
from django.views.decorators.csrf import csrf_exempt
import uuid
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

def short(request):    
    if request.method == 'POST':
        user = request.COOKIES.get('key')
        url = request.POST['link']
        if url.find('<name of your domain>') != -1:
            return render(request, 'index.html', {'status': 'Funny'})  #dynamic data onto your HTML template
        http = urllib3.PoolManager()
        valid = False
        if url.startswith("http"):            
            url = url    
        else:
            url = "http://"+url
        
        try:
            ret = http.request('GET',url)
            if ret.status == 200:
                valid = True
        except Exception as e:
            valid = False
            
        if valid == True:
            new_url = str(uuid.uuid4())[:5]
            surl = "<name of your domain>"+new_url
            sch = {'uid' : user, 'link' : url, 'new' : surl}
            coll.insert_one(sch)
            return render(request, 'result.html', {'user':user, 'url': url, 'new':surl})           #dynamic data onto your HTML template
        else:
            return render(request, 'index.html', {'status': False})
    return redirect('/')