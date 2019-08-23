from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'pages/index.html')

def post(request):
    return render(request,'pages/doc-post.html')

def get(request):
    return render(request,'pages/doc-get.html')
 
def put(request):
    return render(request,'pages/doc-put.html')   

def delete(request):
    return render(request,'pages/doc-delete.html')