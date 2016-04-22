"""Rainfalldataproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
import app.views
from app.views import Home, success,Choose_county_View, Choose_Rainfall_Month_View




urlpatterns = [
    url(r'^admin/', admin.site.urls),
 
    url(r'success', success.as_view(), name='success'),
    url(r'Choose_county$', Choose_county_View.as_view(), name='Choose_county'),
    url(r'Choose_Rainfall_Month_View$', Choose_Rainfall_Month_View.as_view(), name='Choose_Rainfall_Month_View'),
    url(r'^weather_chart_view$', app.views.weather_chart_view, name='weather_chart_view'),
    url(r'^Rainfall_per_month_chart_view$', app.views.Rainfall_per_month_chart_view, name='Rainfall_per_month_chart_view'),
    url(r'^', Home.as_view(), name='Home'),
]
