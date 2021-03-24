from django.urls import path
from crypto_api import views


urlpatterns = [
    path('crypto/', views.CryptoApiView.as_view()),
    path('crypto/<int:pk>/', views.CryptoApiView.as_view(), name='crypto'),
]
