from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import imsUser
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

"""
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        token['username'] = user.username
        return token
"""

class registerSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=imsUser.objects.all())]
    )

    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = imsUser
        fields = ('username', 'password',
                  'password2', 'email',
                  'name', 'Landline_number',
                  'mobile_number', 'address',
                  'is_employee', 'is_customer',
                  )
        extra_kwargs = {
            'name': {'required': True},
            'address': {'required': True},
            'Landline_number': {'required': False},
            'mobile_number': {'required': False},
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match!"})

        return attrs

    def create(self, validated_data):
        user = imsUser.objects.create(
            username=validated_data.get('username'),
            email=validated_data.get('email'),
            name=validated_data.get('name'),
            Landline_number=validated_data.get('Landline_number', '000000000'),
            mobile_number=validated_data.get('mobile_number', '000000000'),
            address=validated_data.get('address'),
            is_employee=validated_data.get('is_employee'),
            is_customer=validated_data.get('is_customer'),
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


class changePasswordSerializer(serializers.ModelSerializer):
    new_password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    new_password2 = serializers.CharField(write_only=True, required=True)
    old_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = imsUser
        fields = ('old_password', 'new_password', 'new_password2')

    def validate(self, attrs):
        if attrs['new_password'] != attrs['new_password2']:
            raise serializers.ValidationError(
                {"new_password": "Password fields didn't match"})

        return attrs

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError(
                {"old_password": "Old password not correct!"})
        return value

    def update(self, instance, validated_data):
        instance.set_password(validated_data['new_password'])
        instance.save()

        return instance


class updateProfileSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)

    class Meta:
        model = imsUser
        fields = ('username', 'email',
                  'name', 'Landline_number',
                  'mobile_number', 'address',
                  'is_employee', 'is_customer',
                  )

        extra_kwargs = {
            'name': {'required': True},
            'address': {'required': True},
            'Landline_number': {'required': False},
            'mobile_number': {'required': False},
        }

    def validate_email(self, value):
        user = self.context['request'].user
        if imsUser.objects.exclude(pk=user.pk).filter(email=value).exists():
            raise serializers.ValidationError(
                {"email": "This Email already in use!"})
        return value

    def validate_username(self, value):
        user = self.context['request'].user
        if imsUser.objects.exclude(pk=user.pk).filter(username=value).exists():
            raise serializers.ValidationError(
                {"username": "This username already exists!"})
        return value

    def update(self, instance, validated_data):

        user = self.context['request'].user

        if user.pk != instance.pk:
            raise serializers.ValidationError(
                {"authorize": "You don't have permission to update profile for this user!"})

        instance.username = validated_data.get('username')
        instance.email = validated_data.get('email')
        instance.name = validated_data.get('name')
        instance.Landline_number = validated_data.get(
            'Landline_number', '+000000000')
        instance.mobile_number = validated_data.get(
            'mobile_number', '+9999999999')
        instance.address = validated_data.get('address')
        instance.is_employee = validated_data.get('is_employee')
        instance.is_customer = validated_data.get('is_customer')

        instance.save()

        return instance
