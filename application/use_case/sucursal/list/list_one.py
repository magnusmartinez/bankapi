from rest_framework.generics import RetrieveAPIView
from infrastructure.entities.models import Sucursal
from infrastructure.serializers.sucursal import  SerializerSucursalListOne


 
class SucursalListOne(RetrieveAPIView): 
    """Listar una sucursal"""

    serializer_class = SerializerSucursalListOne

    def get_queryset(self):

        queryset = Sucursal.objects.filter(is_active=True, id=self.kwargs.get("pk"))
        return queryset
        