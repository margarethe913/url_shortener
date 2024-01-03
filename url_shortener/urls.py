
# djangotemplates/example/urls.py

# from django.conf.urls import url
# from example import views

# urlpatterns = [
#     url(r'^$', views.HomePageView.as_view(), name='home'), # Notice the URL has been named
#     url(r'^about/$', views.ResultPageView.as_view(), name='result'),
# ]

from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'), # Notice the URL has been named
    path('result/', views.ResultPageView.as_view(), name='result'),
]