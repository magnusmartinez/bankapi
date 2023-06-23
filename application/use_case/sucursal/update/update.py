from rest_framework.generics import UpdateAPIView
from infrastructure.entities.models import Sucursal
from infrastructure.serializers.sucursal import  SerializerSucursalUpdate



class SucursalUpdate(UpdateAPIView):
    """Actualizar una sucursal."""
    serializer_class = SerializerSucursalUpdate

    def get_queryset(self):

        queryset = Sucursal.objects.filter(is_active=True,  id=self.kwargs.get("pk", 0))
        return queryset
        