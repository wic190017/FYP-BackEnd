from django.urls import path
from .views import ArticleAPIView,GenericAPIList

urlpatterns = [
    #path('article/', ArticleAPIView.as_view()),
    path('asset/<int:id>/', GenericAPIList.as_view()),
    path('asset/', GenericAPIList.as_view()),
]
