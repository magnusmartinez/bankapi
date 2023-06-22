from rest_framework.generics import ListAPIView
from infrastructure.entities.models import Transaction
from infrastructure.serializers.transaction import  SerializerTransactionList


class TransactionList(ListAPIView): 
    """Listar todas las transacciones realizadas activas"""
    queryset = Transaction.objects.filter(is_active=True).order_by("create_at")
    serializer_class = SerializerTransactionList

