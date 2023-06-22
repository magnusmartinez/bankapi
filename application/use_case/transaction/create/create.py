from rest_framework.generics import CreateAPIView
from infrastructure.entities.models import Transaction
from infrastructure.serializers.transaction import SerializerTransactionCreate


class TransactionCreate(CreateAPIView):  
    """Crear una transacción"""
    
    serializer_class = SerializerTransactionCreate
