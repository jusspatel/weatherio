from django.urls import path 
from . import views
from .views import index

  
urlpatterns = [ 
         path('', views.index), 
] 
