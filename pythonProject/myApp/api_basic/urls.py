from django.urls import path
from .views import ReportList,GenericAPIList

urlpatterns = [
    path('asset/<int:id>/', GenericAPIList.as_view()),
    path('asset/', GenericAPIList.as_view()),
    path('report/', ReportList.as_view()),
    path('report/<int:id>/', ReportList.as_view()),
]


