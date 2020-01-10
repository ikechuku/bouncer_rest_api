from rest_framework import serializers
from ..models.user import User


class UserSerializer(serializers.ModelSerializer):
    
    confirm_password = serializers.CharField(style={'input_type': 'password'}, write_only = True)
    
    class Meta:
        model = User
        fields = '__All__'
        extra_kwargs = {
            'password': { 'write_only': True}
        }

        # overide the save method to confirm the password
        def save(self):
            user = User(
                user_name = self.validated_data(['user_name'])
            )

            password = self.validated_data(['password'])
            confirm_password = self.validated_data(['confirm_password'])

            if password != confirm_password:
                raise serializers.ValidationError({'password': 'password must match'})

            user.set_password(password)
            user.save()
            return user
        

