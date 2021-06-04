from .models import categories, subCategories
from rest_framework import serializers
from datetime import datetime

"""
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        token['username'] = user.username
        return token
"""

class categorySerializer(serializers.ModelSerializer):

    class Meta:
        model = categories
        fields = ('id', 'title',
                  'url_slug',
                  'description',
                  'created_at',
                  'is_active',
                  )
        extra_kwargs = {
            'title': {'required': True},
            'url_slug': {'required': True},
            'created_at': {'required': True},
            'is_active': {'required': True},
            'description': {'required': True},
        }


    def create(self, validated_data):
        category = categories.objects.create(
            title=validated_data.get('title'),
            url_slug = validated_data.get('url_slug'),
            created_at=validated_data.get('created_at'),
            is_active=validated_data.get('is_active'),
            description=validated_data.get('description'),
        )

        category.save()

        return category


    def update(self, instance, validated_data):
        instance.title = validated_data.get('title')
        instance.url_slug = validated_data.get('url_slug')
        instance.created_at = validated_data.get('created_at')
        instance.is_active = validated_data.get('is_active')
        instance.description = validated_data.get('description')
        instance.created_at = datetime.now()
        instance.save()

        return instance


class subCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = subCategories
        fields = ('category_id',
                  'title',
                  'url_slug',
                  'description',
                  'created_at',
                  'is_active',
                  )
        extra_kwargs = {
            'category_id': {'required': True},
            'title': {'required': True},
            'created_at': {'required': True},
            'is_active': {'required': True},
            'description': {'required': True},
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

    '''
    def update(self, instance, validated_data):

        instance.title = validated_data.get('title')
        instance.url_slug = validated_data.get('url_slug')
        instance.created_at = validated_data.get('created_at')
        instance.is_active = validated_data.get('is_active')
        instance.description = validated_data.get('description')

        instance.save()

        return instance
    '''