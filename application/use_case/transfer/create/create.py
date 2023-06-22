from rest_framework.generics import CreateAPIView
from infrastructure.entities.models import Transfer
from infrastructure.serializers.transfer import SerializerTransferCreate


class TransferCreate(CreateAPIView):  
    """Crear una transferencia entre cuentas."""
    
    serializer_class = SerializerTransferCreate
