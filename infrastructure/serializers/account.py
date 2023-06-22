from rest_framework import serializers
from infrastructure.entities.models import Account
from application.use_case.utils import constants as cts
from random import random

class SerializerAccountCreate(serializers.ModelSerializer):
    """
    Serializer del modelo Account para crear un registro
    """

    class Meta:
        model = Account
        exclude = ["number"]
    
    def create(self, validated_data):
        validated_data['number'] = self.get_random_number()
        instance = Account.objects.create(**validated_data)
        return instance

    def get_random_number(self):
        """Returns a random string that represent the account number."""
        limit = 15
        while limit >= 1:
            number = str(random()).split('.')[1][:cts.MAXIMUM_LENGTH_ACCOUNT_ALLOWED]
            if not Account.objects.filter(number=number).exists():
                return number 
            limit -= 1
    
class SerializerAccountUpdate(serializers.ModelSerializer):
    """
    Serializer del modelo Account para actualizar un registro
    """

    class Meta:
        model = Account
        exclude = ["owner", "number"]


class SerializerAccountList(serializers.ModelSerializer):
    """
    Serializer del modelo Account para listar todos los registros
    """
    
    class Meta:
        model = Account
        fields = "__all__"

class SerializerAccountByOwner(serializers.ModelSerializer):
    """
    Serializer del modelo Account para listar todos los registros de un cliente (Owner)
    """
    
    class Meta:
        model = Account
        fields = "__all__"
        lookup_field = "owner"
        depth = 2



class SerializerAccountListOne(serializers.ModelSerializer):
    """
    Serializer del modelo Account para listar un registro
    """

    class Meta:
        model = Account
        fields = "__all__"
        depth = 2
