from django.shortcuts import render

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from tutorial.quickstart.serializers import *
from tutorial.quickstart.models import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from rest_framework.permissions import IsAuthenticated



class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


#**************************************************************#
class AlumnoViewSet(viewsets.ModelViewSet):

    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer

@api_view(['GET', 'PUT', 'DELETE'])
def Alumno_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Alumno.objects.get(pk=pk)
    except Alumno.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AlumnoSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = AlumnoSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
#**************************************************************#

class ClasesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Clases.objects.all()
    serializer_class = ClasesSerializer

@api_view(['GET', 'PUT', 'DELETE'])
def Calses_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Clases.objects.get(pk=pk)
    except Clases.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ClasesSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ClasesSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

##################
class AsistenciaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Asistencia.objects.all()
    serializer_class = AsistenciaSerializer

@api_view(['GET', 'PUT', 'DELETE'])
def Asistencia_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Asistencia.objects.get(pk=pk)
    except Asistencia.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AsistenciaSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = AsistenciaSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#########################

