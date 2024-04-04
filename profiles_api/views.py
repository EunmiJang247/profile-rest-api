from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions

# Create your views here.
class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer #요청보낼 때 name은 10글짜 까지만이야.

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over you application logic',
            'Is mapped manually to URLs',
        ]
        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        """ Create Hello message with our name """
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )

    def put(self, request, pk=None):
        """Handle updating an object"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'messagePut': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )

        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle partial update of object"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'messagePatch!': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )

        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""

        return Response({'method': 'DELETE'})

class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class = serializers.HelloSerializer

    # http://localhost:8000/api/hello-viewset/로 접속 시
    def list(self, request):
        """Return Hello message"""
        a_viewset = [
            'Uses action (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLs sing Routers',
            'Proivides more functioanliy with less code',
        ]

        return Response({'message': 'Hello', 'a_viewset': a_viewset})

    # Create 기능 POST Name에 넣어야함. HTML form / Raw data에 넣기
    def create(self, request):
        """ create a new hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    # http://localhost:8000/api/hello-viewset/1/ 이렇게 보낸경우.
    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""

        return Response({'http_method': 'GET'})
    # PUT버튼 누른 경우
    def update(self, request, pk=None):
        """Handle updating an object"""

        return Response({'http_method': 'PUT'})
    # PATCH버튼 누른 경우
    def partial_update(self, request, pk=None):
        """Handle updating part of an object"""

        return Response({'http_method': 'PATCH'})
    # DELETE버튼 누른 경우
    def destroy(self, request, pk=None):
        """Handle removing an object"""

        return Response({'http_method': 'DELETE'})

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating, creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication, )
    permission_classes = (permissions.UpdateOwnProfile,  )
    filter_backends = (filters.SearchFilter, )
    search_fields = ('name', 'email',)

class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
