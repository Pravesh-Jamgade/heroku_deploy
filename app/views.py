from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from app.models import Welcome
from app.serializer import WelcomeSerializer

# Create your views here.

class WelcomeViewSet(viewsets.ModelViewSet):
    queryset = Welcome.objects.all()
    serializer_class = WelcomeSerializer

    @action(detail=True, methods=['post'])
    def post(self, request):
        print('hell with it \n')
        msg = ""
        serializer = WelcomeSerializer(request.data)
        if serializer.is_valid():
            msg = serializer.data['message']
            serializer.save()
            return Response({'status': 201, 'message':msg})
        return Response({'status':400, 'message':"Bad Request"})
            