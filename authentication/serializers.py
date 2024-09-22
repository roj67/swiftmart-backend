from rest_framework.serializers import ModelSerializer
from .models import User

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'address', 'number', 'password']

    def create(self, validated_data):
        extra_fields = {
            "number" : validated_data["number"],
            "address" : validated_data["address"],
            "username" : validated_data["username"]
        }
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            **extra_fields
        )
        return user