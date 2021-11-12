from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from .serializers import CurrencySerializer

from ..models import Currency


class CurrencyPagination(PageNumberPagination):

    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 10


class CurrenciesListApiView(ListAPIView):

    serializer_class = CurrencySerializer
    pagination_class = CurrencyPagination
    queryset = Currency.objects.all().order_by('id')


class CurrencyDetailApiView(RetrieveAPIView):

    serializer_class = CurrencySerializer
    queryset = Currency.objects.all()
