from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status

from . import serializers

# Create your views here.
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