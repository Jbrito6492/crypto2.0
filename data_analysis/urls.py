from data_analysis import views
from django.urls import path, include

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', views.DataViewSet, basename='data-viewset')

urlpatterns = [
    path('', include(router.urls))

]
