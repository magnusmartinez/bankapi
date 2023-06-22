from infrastructure.entities.models import User
from rest_framework.generics import DestroyAPIView


class UserDelete(DestroyAPIView):
    """Eliminar un registro. No fisicamente en la base de datos, solo cambia is_active a False"""
    queryset = User.objects.all()

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()



