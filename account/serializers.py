from rest_framework import serializers

from .models import User


class RegisterSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(max_length=4)

    class Meta:
        model = User
        fields = ('email', 'password', 'password_confirm')\
    

    def validate(self, attrs):
        pass1 = attrs.get('password')
        pass2 = attrs.get('password_confirm')

        if pass1 != pass2:
            raise serializers.ValidationError('Password dont match')
        
        return attrs
    

    def email_validate(self, email):
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError('Email already exists')
        
        return email

    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
