from .models import categories, subCategories, products
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
        fields = ('id',
                  'category_id',
                  'title',
                  'url_slug',
                  'description',
                  'created_at',
                  'is_active',
                  )
        extra_kwargs = {
            'category_id': {'required': True},
            'title': {'required': True},
            'url_slug': {'required': True},
            'created_at': {'required': True},
            'is_active': {'required': True},
            'description': {'required': True},
        }

    def create(self, validated_data):
        sub_category = subCategories.objects.create(
            id=validated_data.get('id'),
            category_id = validated_data.get("category_id"),
            url_slug = validated_data.get("url_slug"),
            title=validated_data.get('title'),
            created_at=validated_data.get('created_at'),
            is_active=validated_data.get('is_active'),
            description=validated_data.get('description'),

        )

        sub_category.save()

        return sub_category


    def update(self, instance, validated_data):

        instance.category_id = validated_data.get('category_id')
        instance.title = validated_data.get('title')
        instance.url_slug = validated_data.get('url_slug')
        instance.is_active = validated_data.get('is_active')
        instance.description = validated_data.get('description')
        instance.created_at = datetime.now()

        instance.save()

        return instance


class productSerializer(serializers.ModelSerializer):
    class Meta:
        model = products
        fields = ('url_slug',
                'sub_categories_id',
                'product_name',
                'brand',
                'product_max_price',
                'product_discount_price',
                'product_description',
                'product_long_description',
                'created_at',
                #'added_by_staff',
                'total_stock',
                'is_active',
                )


        # def validate_sub_categories_id(self,value):
        #     try:
        #         subCategories.objects.get(id=value)
        #         return value
        #     except:
        #         pass
            
        extra_kwargs = {
            'url_slug': {'required': True},
            'sub_categories_id': {'required': True},
            'product_name': {'required': True},
            'brand': {'required': True},
            'product_max_price': {'required': True},
            'product_discount_price': {'required': True},
            'product_description': {'required': True},
            'product_long_description': {'required': False},
            'created_at': {'required': True},
            #'added_by_staff': {'required': True},
            'is_active': {'required': True},
            'total_stock': {'required': True},
        }


    def create(self, validated_data):

        product = products.objects.create(
            sub_categories_id = validated_data.get("sub_categories_id"),
            url_slug = validated_data.get("url_slug"),
            product_name = validated_data.get('product_name'),
            brand = validated_data.get('brand'),
            product_max_price = validated_data.get('product_max_price'),
            product_discount_price = validated_data.get('product_discount_price'),
            product_description = validated_data.get('product_description'),
            #added_by_staff = validated_data.get('added_by_staff'),
            is_active = validated_data.get('is_active'),
            total_stock = validated_data.get('total_stock'),
        )

        product.save()

        return product

    def update(self, instance, validated_data):
        print(validated_data.get("sub_categories_id"))
        instance.sub_categories_id = validated_data.get("sub_categories_id",instance.sub_categories_id)
        instance.url_slug = validated_data.get("url_slug",        instance.url_slug )
        instance.product_name = validated_data.get('product_name' ,        instance.product_name )
        instance.brand = validated_data.get('brand',        instance.brand )
        instance.product_max_price = validated_data.get('product_max_price',        instance.product_max_price )
        instance.product_discount_price = validated_data.get('product_discount_price',        instance.product_discount_price )
        instance.product_long_description = validated_data.get('product_long_description',        instance.product_long_description )
        # added_by_staff = validated_data.get('added_by_staff',        # added_by_staff ),
        instance.is_active = validated_data.get('is_active' ,        instance.is_active )
        instance.total_stock = validated_data.get('total_stock',        instance.total_stock )
        instance.save()

        return instance