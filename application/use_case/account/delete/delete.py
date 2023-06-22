from infrastructure.entities.models import Account
from rest_framework.generics import DestroyAPIView


class AccountDelete(DestroyAPIView):
    """Eliminar un registro. No fisicamente en la base de datos, solo cambia is_active a False."""

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()

    def get_queryset(self):
        queryset = Account.objects.filter(id=self.kwargs.get("pk"))
        return queryset
        