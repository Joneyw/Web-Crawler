"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from blog  import views 

urlpatterns = [
    
    
    url(r'^show_movie/', views.show_movie,name="movieinfo"), 
    url(r'^$', views.login), 
    url(r'^admin/', admin.site.urls),
    url(r'^show_weather/', views.show_weather,name="weatherinfo"), 
    url(r'^search_weather/', views.search_weather,name="search_weather"), 
    url(r'^show_goods/',views.show_goods,name='goodsinfo')
]
