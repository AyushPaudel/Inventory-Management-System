from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import categories
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken


"""
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        token['username'] = user.username
        return token
"""

class registerSerializer(serializers.ModelSerializer):
    # email = serializers.EmailField(
    #     required=True,
    #     validators=[UniqueValidator(queryset=categories.objects.all())]
    # )

    slug = serializers.CharField(
        write_only=True, required=True)
    slug2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = categories
        fields = ('id', 'title',
                  'slug', 'slug2',
                  'description', 'dealer',
                  )
        extra_kwargs = {
            'id': {'required': True},
            'title': {'required': True},
            'description': {'required': False},
            'dealer': {'required': False},
        }

    def validate(self, attrs):
        if attrs['slug'] != attrs['slug2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match!"})

        return attrs

    def create(self, validated_data):
        category = categories.objects.create(
            id=validated_data.get('id'),
            title=validated_data.get('title'),
            description=validated_data.get('description'),
            dealer=validated_data.get('dealer'),

        )

        category.set_password(validated_data['password'])
        category.save()

        return category
