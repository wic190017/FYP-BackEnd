from rest_framework import serializers
from .models import Asset

class ArticleSerializers(serializers.ModelSerializer):

    lookup_field = 'id'

    class Meta:
        model = Asset
        fields = '__all__'
