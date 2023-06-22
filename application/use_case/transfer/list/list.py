from rest_framework.generics import ListAPIView
from infrastructure.entities.models import Transfer
from infrastructure.serializers.transfer import  SerializerTransferList


class TransferList(ListAPIView): 
    """Listar todas las transferencias realizadas activas"""
    queryset = Transfer.objects.filter(is_active=True).order_by("create_at")
    serializer_class = SerializerTransferList

