from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class RegisterSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(
        required = True,
        validators = [UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(
        write_only = True,
        required = True,
        validators = [validate_password],
        style = {
            'input_type' : 'password'
        }
    )

    password2 = serializers.CharField(
        write_only = True,
        required = True,
        style = {
            'input_type' : 'password'
        }
    )

    class Meta:
        model = User
        fields = (
            'username',
            'password',
            'password2',
            'email',
        )

    def validate(self, data):
        if data.get('password') != data.get('password2'):
            raise serializers.ValidationError(
                {'password':'Passwords must match!!!'}
            )
        return data
    
    def create(self, validated_data):
        validated_data.pop('password2')
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user