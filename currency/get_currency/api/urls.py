from django.urls import path

from .api_views import CurrencyDetailApiView, CurrenciesListApiView

urlpatterns = [
    path('currencies/', CurrenciesListApiView.as_view(), name='currencies'),
    path('currency/<int:pk>/', CurrencyDetailApiView.as_view(), name='currency'),
]