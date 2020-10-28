from django.urls import path
from . import views


urlpatterns = [
        path('',views.index,name='index'),
        path('create', views.create, name='create'),
       # path('test',views.test,name='test'),
        #path('form', views.form, name='form'),
]
