from data_analysis import views
from django.urls import path


urlpatterns = [
    path('<int:pk>/', views.DataViewApi.as_view(), name='analysis')
]
