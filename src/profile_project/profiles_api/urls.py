from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^hello-view/', views.HelloApi.as_view(), name='hello-view'),
]