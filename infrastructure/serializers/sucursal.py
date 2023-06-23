from rest_framework import serializers
from infrastructure.entities.models import Sucursal
from django.forms.models import model_to_dict


class SerializerSucursalCreate(serializers.ModelSerializer):
    """
    Serializer del modelo Sucursal para crear un registro
    """

    class Meta:
        model = Sucursal
        exclude = ["is_active"]



class SerializerSucursalUpdate(serializers.ModelSerializer):
    """
    Serializer del modelo Sucursal para actualizar un registro
    """

    class Meta:
        model = Sucursal
        fields = "__all__"


class SerializerSucursalList(serializers.ModelSerializer):
    """
    Serializer del modelo Sucursal para listar todos los registros
    """
    
    class Meta:
        model = Sucursal
        fields = "__all__"

class SerializerSucursalListOne(serializers.ModelSerializer):
    """
    Serializer del modelo Sucursal para listar un registro
    """

    class Meta:
        model = Sucursal
        fields = "__all__"
        # depth = 2
