from django.contrib.auth.models import User, Group
from rest_framework import serializers
from tutorial.quickstart.models import Alumno, Clases, Asistencia


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

###
class AlumnoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Alumno
        fields = ['nomUsuario','nombre','apellidoP','apellidoM','rut', 'contraseña','correo']

class ClasesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Clases
        fields = ['nombre', 'sigla']

class AsistenciaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Asistencia
        fields = ['nombreAlum', 'rutAlum']

