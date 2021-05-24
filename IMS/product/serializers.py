from .models import categories, subCategories
from rest_framework import serializers


"""
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        token['username'] = user.username
        return token
"""

class addCategory(serializers.ModelSerializer):

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


class addSubCategory(serializers.ModelSerializer):

    class Meta:
        model = subCategories
        fields = ('id', 'category_id',
                  'title',
                  'url_slug',
                  'description',
                  'created_at',
                  'is_active',
                  )
        extra_kwargs = {
            'id': {'required': True},
            'category_id': {'required': True},
            'title': {'required': True},
            'created_at': {'required': True},
            'is_active': {'required': True},
            'description': {'required': False},
        }

    def create(self, validated_data):
        sub_category = subCategories.objects.create(
            id=validated_data.get('id'),
            category_id = validated_data.get("category_id"),
            title=validated_data.get('title'),
            created_at=validated_data.get('created_at'),
            is_active=validated_data.get('is_active'),
            description=validated_data.get('description'),

        )

        sub_category.save()

        return sub_category

