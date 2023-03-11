from django.contrib import admin
from django.urls import path
from pybo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.get_info, name = 'info'),
    path('param/', views.parameters, name='param'),
    path('popup/', views.popup, name='popup'),
    path('submit_url/', views.submit_url, name='submit_url'),
    path('result/', views.show_result, name = "result")
]
