from rest_framework import serializers
from infrastructure.entities.models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.serializers import RefreshToken, PasswordField
from django.forms.models import model_to_dict


class SerializerUserCreate(serializers.ModelSerializer):
    """
    Serializer del modelo User para crear un usuario
    """

    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
    
        # se crea manualmente el usuario para poder hacer que la 
        # password sea encriptada utilizando el medoto set_password

        groups = validated_data.pop("groups")
        user_permissions = validated_data.pop("user_permissions")

        instance = User.objects.create(**validated_data)

        # se asignan los grupos y los permisos de esta forma por ser campos de tipo ManyToMany
        instance.groups.set(groups)
        instance.user_permissions.set(user_permissions)

        instance.set_password(validated_data['password'])


        instance.save()

        return instance
    
    def to_representation(self, instance):

        return model_to_dict(instance, exclude=["password"]) 


class SerializerUserUpdate(serializers.ModelSerializer):
    """
    Serializer del modelo User para actualizar un registro
    """

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "is_staff", "is_superuser", "image"]


class SerializerUserList(serializers.ModelSerializer):
    """
    Serializer del modelo User para listar todos los registros
    """
    
    class Meta:
        model = User
        exclude = ["password"]

class SerializerUserListOne(serializers.ModelSerializer):
    """
    Serializer del modelo User para listar un registro
    """
    
    class Meta:
        model = User
        exclude = ["password"]



#Custom Token Obtain Serializer
class SerializerUserLogin(serializers.Serializer):

    token_class = RefreshToken
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
 
    def validate(self, data):
        user = authenticate(username=data["username"], password=data["password"])
        if user is None:
            raise serializers.ValidationError("Invalid username/password")

        refresh = RefreshToken.for_user(user)
        data["access"] = str(refresh.access_token)
        data["refresh"] = str(refresh)
        data["username"] = user.username
        data["user_id"] = user.id

        data.pop("password", None)
        return data
  
