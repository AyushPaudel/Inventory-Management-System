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

class addCategory(serializers.ModelSerializer):
    # email = serializers.EmailField(
    #     required=True,
    #     validators=[UniqueValidator(queryset=categories.objects.all())]
    # )



    class Meta:
        model = categories
        fields = ('id', 'title',
                  'url_slug',
                  'description',
                  'created_at',
                  'is_active',
                  )
        extra_kwargs = {
            'id': {'required': True},
            'title': {'required': True},
            'created_at': {'required': True},
            'is_active': {'required': True},
            'description': {'required': False},
        }

    def create(self, validated_data):
        category = categories.objects.create(
            id=validated_data.get('id'),
            title=validated_data.get('title'),
            created_at=validated_data.get('created_at'),
            is_active=validated_data.get('is_active'),
            description=validated_data.get('description'),

        )

        category.save()

        return category
