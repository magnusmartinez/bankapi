from rest_framework import serializers
from infrastructure.entities.models import Client
# from django.db.models import Q


class SerializerClientCreate(serializers.ModelSerializer):
    """
    Serializer del modelo Client para crear un registro
    """

    class Meta:
        model = Client
        fields = "__all__"


class SerializerClientUpdate(serializers.ModelSerializer):
    """
    Serializer del modelo Client para actualizar un registro
    """

    class Meta:
        model = Client
        fields = "__all__"


class SerializerClientList(serializers.ModelSerializer):
    """
    Serializer del modelo Client para listar todos los registros
    """
    
    class Meta:
        model = Client
        fields = "__all__"


class SerializerClientBySucursal(serializers.ModelSerializer):
    """
    Serializer del modelo Client para listar todos los registros de una sucursal
    """
    
    class Meta:
        model = Client
        fields = "__all__"
        lookup_field = "sucursal"


class SerializerClientListOne(serializers.ModelSerializer):
    """
    Serializer del modelo Client para listar un registro
    """

    class Meta:
        model = Client
        fields = "__all__"
        depth = 2
