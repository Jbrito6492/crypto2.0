from crypto_api import views
from django.urls import path


urlpatterns = [
    path('crypto/', views.CryptoApiView.as_view(), name='crypto'),
    path('crypto/<int:pk>/', views.CryptoApiView.as_view(), name='crypto_id'),
]
