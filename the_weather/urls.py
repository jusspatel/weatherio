from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404, handler500
from main import views as myapp_views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    
]
handler404 = myapp_views.error_404
handler500 = myapp_views.error_500
