from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class HelloApi(APIView):
    """Test Api View."""

    def get(self, request, format=None):
        """Returns a list of apiview features"""

        an_apiview = [
            'Uses Http methods as function (get, post, patch, put, delete)',
            'Its Similar to tredinational django view',
            'gives you most control over your logic',
            'it maped manullay to url',
        ]

        return Response({'message':'hello api!', 'an_apiview': an_apiview})