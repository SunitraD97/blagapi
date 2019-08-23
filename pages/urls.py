from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    #path('about', views.about, name='about'),
    path('post', views.post, name="post"),
    path('get', views.get, name="get"),
    path('put', views.put, name="put"),
    path('delete', views.delete, name="delete"),
]
