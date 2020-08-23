from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers
from rest_framework import status

from rest_framework import viewsets

class HelloApiView(APIView):
    #test api view

    serializer_class = serializers.helloserializers

    def get(self, request, format = None):
        #returns a list of api view features

        an_apiview = [
            'uses http methods like get, post, patch, put, delete as functions',
            'it is similar to a traditional django view',
            'gives u the most control over ur logic',
            'its mapped manually to the urls'
        ]

        return Response({'message' : 'hello' , 'an_apiview' : an_apiview})
#now we need to map a url to this api so that it can be acceseed with an http server ... shit means nothing bt taking it to the urls.py


    def post(self, request):
        #create a hello message with our name given by the serializer

        serializer = serializers.helloserializers(data = request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'hello {0}'.format(name)
            return Response({'message' : message})
        else:
            return Response(
                serializer.errors, status = status.HTTP_400_BAD_REQUEST
            )
    
class helloviewset(viewsets.ViewSet):
    #test api viewset

    def list(self, request):
        #returns a hello message

        a_viewset = [
            'uses actions (list, create, retrieve, update, partial_update)',
            'a viewset automatically maps to the urls using routers',
            'a viewset provides most functionality with less code'
        ]

        return Response({'message' : 'helllo' , 'a_viewset' : a_viewset})