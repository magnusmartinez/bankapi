from rest_framework.generics import UpdateAPIView
from infrastructure.entities.models import Transfer
from infrastructure.serializers.transfer import  SerializerTransferUpdate



class TransferUpdate(UpdateAPIView):
    """Actualizar una cuenta."""
    serializer_class = SerializerTransferUpdate

    def get_queryset(self):

        queryset = Transfer.objects.filter(is_active=True,  id=self.kwargs.get("pk", 0))
        return queryset
        