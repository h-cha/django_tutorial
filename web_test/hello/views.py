# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from .forms import HelloForm

# Create your views here.

def index(request):
    params = {
        #'sample' : 'こんにちは',
        #'bun' : 'djangoたのしい',
        #'memo':'次のぺーじ',     
        #'nextpage' : 'test',
        'title' : 'Hello/Home',
        'message' : 'data',
        'form' : HelloForm()
    }
    if (request.method == 'POST'):
        params['message'] = '名前:' + request.POST['name'] + '<br>メール:' + request.POST['mail'] + '<br>年齢:' + request.POST['age']
        params['form'] = HelloForm(request.POST)
    return render(request, 'hello/index.html',params)

def test(request):
    params = {
        'sample' : 'さようなら',
        'bun' : 'djangoつまんない',
        'memo':'次のぺーじ',
        'nextpage' : 'index',
    }
    return render(request, 'hello/index.html',params)

def form(request):
    msg = request.POST['msg']
    params = {
        'title' : 'Hello/Form',
        'msg' : 'こんにちは' + msg + 'さん。',
    }
    return render(request, 'hello/index.html', params)