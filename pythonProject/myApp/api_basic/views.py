from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Asset
from .models import Report
from .serializers import ArticleSerializers
from .serializers import ReportSerializers
from rest_framework import generics
from rest_framework import mixins


# Create your views here.

# class GenericAPIList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
#     serializer_class = ArticleSerializers
#     queryset = Asset.objects.all()
#
#     lookup_field = 'id'
#
#     def get(self, request, id=None):
#         return self.list(request)
#
#     def post(self, request):
#         return self.create(request)


# 1.28.53
class GenericAPIList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin,
                       mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class = ArticleSerializers
    queryset = Asset.objects.all()

    lookup_field = 'id'

    def get(self, request, id=None):
        if id:
            return self.retrieve(request, id)
        else:
            return self.list(request, id)

    def post(self, request):
        return self.create(request)

    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id):
        return self.destroy(request, id)

class ReportList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin,
                       mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class = ReportSerializers
    queryset = Report.objects.all()

    lookup_field = 'id'

    def get(self, request, id=None):
        if id:
            return self.retrieve(request, id)
        else:
            return self.list(request, id)

    def post(self, request):
        return self.create(request)

    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id):
        return self.destroy(request, id)