from rest_framework import serializers
from infrastructure.entities.models import Transfer
from infrastructure.entities.transfer.transfer import STATUS_CHOICES
from application.use_case.utils import constants as cts
from random import random
from django.forms.models import model_to_dict


class SerializerTransferCreate(serializers.ModelSerializer):
    """
    Serializer del modelo Transfer para crear un registro
    """

    class Meta:
        model = Transfer
        exclude = ["code", "status", "is_active"]
    
    def create(self, validated_data):
        
        source_account = validated_data.get("source_account")
        destination_account = validated_data.get("destination_account")

        amount = validated_data.get("amount")
        commission = amount * cts.TRANSFER_COMMISSION_PERCENTAGE
        real_amount = amount + commission
    
        validated_data["status"] = STATUS_CHOICES[0][0]
        validated_data["commission"] = cts.TRANSFER_COMMISSION_PERCENTAGE
        validated_data["code"] = self.get_random_code()
        instance = Transfer.objects.create(**validated_data)

        if (source_account.balance - real_amount) >= cts.MINIMUM_BALANCE_ACCOUNT_LIMIT_ALLOWED :

            source_account.balance -= real_amount
            destination_account.balance += amount

            destination_account.save()
            source_account.save()
            instance.status = STATUS_CHOICES[1][0]
            instance.save()
        else:
            instance.status = STATUS_CHOICES[2][0]
            instance.save()

        return instance


    def to_representation(self, instance):

        return model_to_dict(instance)

    def get_random_code(self):
        """Returns a random string that represent the code transfer."""
        limit = 15
        while limit >= 1:
            code = str(random()).split('.')[1][:cts.DIFAULT_LENGHT_CODE_TRANSFER]
            if not Transfer.objects.filter(code=code).exists():
                return code 
            limit -= 1



# class SerializerTransferUpdate(serializers.ModelSerializer):
#     """
#     Serializer del modelo Transfer para actualizar un registro
#     """

#     class Meta:
#         model = Transfer
#         exclude = ["reference", "description"]


class SerializerTransferList(serializers.ModelSerializer):
    """
    Serializer del modelo Transfer para listar todos los registros
    """
    
    class Meta:
        model = Transfer
        fields = "__all__"

class SerializerTransferByAccount(serializers.ModelSerializer):
    """
    Serializer del modelo Transfer para listar todos los registros de una sucursal
    """
    
    class Meta:
        model = Transfer
        fields = "__all__"
        lookup_field = "source_account"
        depth = 2

class SerializerTransferByAccounts(serializers.ModelSerializer):
    """
    Serializer del modelo Transfer para listar todos los registros de una sucursal
    """
    
    class Meta:
        model = Transfer
        fields = "__all__"
        lookup_field = "source_account"
        depth = 2



class SerializerTransferListOne(serializers.ModelSerializer):
    """
    Serializer del modelo Transfer para listar un registro
    """

    class Meta:
        model = Transfer
        fields = "__all__"
        depth = 2
