from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status, filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from . import serializers
from . import models
from . import permissions
# Create your views here.

class LoginViewSet(viewsets.ViewSet):
    """Checks email and password and return an auth token."""
    serializer_class = AuthTokenSerializer

    def create(self, request):
        """Use The ObtainAuthToken APIView to validate and create a token."""

        return ObtainAuthToken().post(request)


class ProfileFeedViewSet(viewsets.ModelViewSet):
    """Handles Creating, Redaing, Upadating, Profile Feed item."""

    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (permissions.PostOwnStatus, IsAuthenticatedOrReadOnly, IsAuthenticated)

    def perform_create(self, serializer):
        """Sets The User Profile to the logged in user"""
        serializer.save(user_profile=self.request.user)





class UserProfileViewSet(viewsets.ModelViewSet):
    """handle user profile creating"""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)







class HelloViewset(viewsets.ViewSet):
    """ Test Viewset api """

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a hello meassge."""

        a_viewset = [
            'Uses actions (list, create, retrive, update, partial_update)',
            'Automatically maps to URLs usign Routers',
            'provide more functionality with less code',
        ]

        return Response({'message': 'Hello!', 'a_viewset': a_viewset})
    
    def create(self, request):
        """ crate hello message with our name """

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)

            return Response({'message': message})
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """ Handles getting an object by its id """
        return Response({'http_method': 'GET'})

    def partial_update(self, request, pk=None):
        """ Handle updating part of an object """
        return Response({'http_method': 'PATCH'})

    def update(self, request, pk=None):
        """ Handle upadting part of object """
        return Response({"http_method": "PUT"})
    
    def destroy(self, request, pk=None):
        """ Delete an object """
        return Response({"http_method": "DELETE"})

class HelloApi(APIView):
    """Test Api View."""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of apiview features"""

        an_apiview = [
            'Uses Http methods as function (get, post, patch, put, delete)',
            'Its Similar to tredinational django view',
            'gives you most control over your logic',
            'it maped manullay to url',
        ]

        return Response({'message':'hello api!', 'an_apiview': an_apiview})

    def post(self, request):
        """ crate hello message with our name """

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)

            return Response({'message': message})
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handle updating an objects"""
        return Response({'method': 'put'})

    def patch(self, request, pk=None):
        """Patch request, only updates fields, provided in the request"""
        return Response({'method':'patch'})

    def delete(self, request, pk=None):
        """Delete an objects """
        return Response({'method': 'delete'})