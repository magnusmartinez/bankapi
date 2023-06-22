from rest_framework.generics import RetrieveAPIView
from infrastructure.entities.models import User
from infrastructure.serializers.user import  SerializerUserListOne


 
class UserListOne(RetrieveAPIView): 
    """Lista un usuario"""
    queryset = User.objects.filter(is_active=True)
    serializer_class = SerializerUserListOne

