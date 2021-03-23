from django.urls import path
from crypto_api import views


urlpatterns = [
    path('crypto/', views.CryptoApiView.as_view())
]
