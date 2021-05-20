from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('/inicio', views.inicio, name='blog-inicio'),
    path(r'^/(?P<stream_path>(.*?))/$',views.dynamic_stream,name="videostream"),  
    path(r'^stream/$',views.indexscreen),
]