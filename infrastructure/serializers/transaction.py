from rest_framework import serializers
from infrastructure.entities.models import Transaction
from infrastructure.entities.transaction.transaction import STATUS_CHOICES, TRANSACTION_TYPES_CHOICES
from application.use_case.utils import constants as cts
from random import random
from django.forms.models import model_to_dict


class SerializerTransactionCreate(serializers.ModelSerializer):
    """
    Serializer del modelo Transaction para crear un registro
    """

    class Meta:
        model = Transaction
        exclude = ["is_active", "reference_number", "status"]
        # depth = 2

    def create(self, validated_data):

        validated_data["reference_number"] = self.get_random_reference_number()
        instance = Transaction(**validated_data)
        instance.status = STATUS_CHOICES[0][0]  # transaction pending
        transaction_type = validated_data.get("transaction_type")

        # if transaction is a deposit
        if transaction_type == TRANSACTION_TYPES_CHOICES[0][0]:

            amount = validated_data.get("amount")
            commission = amount * cts.TRANSACTION_DEPOSIT_COMMISSION_PERCENTAGE
            real_amount = amount - commission

            if real_amount >= cts.MINIMUN_DEPOSIT_ALLOWED:

                instance.commission = cts.TRANSACTION_DEPOSIT_COMMISSION_PERCENTAGE
                instance.status = STATUS_CHOICES[1][0]

                destination_account = validated_data.get("destination_account")
                destination_account.balance += real_amount

                # transaction completed
                destination_account.save()
                instance.save()
            else:
                # transaction canceled
                instance.commission = cts.TRANSACTION_DEPOSIT_COMMISSION_PERCENTAGE
                instance.status = STATUS_CHOICES[2][0]
                instance.save()

            return instance

        # if transaction is a withdrawal
        elif transaction_type == TRANSACTION_TYPES_CHOICES[1][0]:  

            amount = validated_data.get("amount")
            commission = amount * cts.TRANSACTION_WITHDRAWAL_COMMISSION_PERCENTAGE
            real_amount = amount + commission
            destination_account = validated_data.get("destination_account")

            if real_amount >= cts.MINIMUN_WITHDRAWAL_ALLOWED and (destination_account.balance - real_amount) >= cts.MINIMUM_BALANCE_ACCOUNT_LIMIT_ALLOWED:
                instance.commission = cts.TRANSACTION_WITHDRAWAL_COMMISSION_PERCENTAGE
                instance.status = STATUS_CHOICES[1][0]

                
                destination_account.balance -= real_amount # withdrawal operation
 
                # transaction completed
                destination_account.save()
                instance.save()
            else: 
                # transaction canceled
                instance.commission = cts.TRANSACTION_WITHDRAWAL_COMMISSION_PERCENTAGE
                instance.status = STATUS_CHOICES[2][0]
                instance.save()

        return instance

    def to_representation(self, instance):

        return model_to_dict(instance)

    def get_random_reference_number(self):
        """Returns a random string that represent the reference_number transaction."""
        limit = 15
        while limit >= 1:
            reference_number = str(random()).split('.')[1][:cts.DIFAULT_LENGHT_CODE_TRANSFER]
            if not Transaction.objects.filter(reference_number=reference_number).exists():
                return reference_number
            limit -= 1


# class SerializerTransactionUpdate(serializers.ModelSerializer):
#     """
#     Serializer del modelo Transaction para actualizar un registro
#     """

#     class Meta:
#         model = Transaction
#         exclude = ["reference", "description"]


class SerializerTransactionList(serializers.ModelSerializer):
    """
    Serializer del modelo Transaction para listar todos los registros
    """

    class Meta:
        model = Transaction
        fields = "__all__"

class SerializerTransactionByDestinationAccount(serializers.ModelSerializer):
    """
    Serializer del modelo Transaction para listar todos los registros de una sucursal
    """

    class Meta:
        model = Transaction
        fields = "__all__"
        lookup_field = "destination_account"
        depth = 2

# class SerializerTransactionByAccounts(serializers.ModelSerializer):
#     """
#     Serializer del modelo Transaction para listar todos los registros de una sucursal
#     """

#     class Meta:
#         model = Transaction
#         fields = "__all__"
#         lookup_field = "source_account"
#         depth = 2


class SerializerTransactionListOne(serializers.ModelSerializer):
    """
    Serializer del modelo Transaction para listar un registro
    """

    class Meta:
        model = Transaction
        fields = "__all__"
        depth = 2
