from rest_framework import serializers
from .models import Asset
from .models import Report


class ArticleSerializers(serializers.ModelSerializer):
    lookup_field = 'id'

    class Meta:
        model = Asset
        fields = '__all__'


class ReportSerializers(serializers.ModelSerializer):
    lookup_field = 'id'

    class Meta:
        model = Report
        fields = '__all__'
