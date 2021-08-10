from product.models import products
from rest_framework.serializers import ModelSerializer

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = products
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style']