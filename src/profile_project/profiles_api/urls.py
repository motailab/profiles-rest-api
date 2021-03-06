from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewset, base_name='hello-viewset')
router.register('profile', views.UserProfileViewSet)
router.register('login', views.LoginViewSet, base_name='login')
router.register('feed', views.ProfileFeedViewSet)

urlpatterns = [
    url(r'^hello-view/', views.HelloApi.as_view(), name='hello-view'),
    url(r'', include(router.urls)),
]