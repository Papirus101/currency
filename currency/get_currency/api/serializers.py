from rest_framework import serializers

from ..models import Currency


class CurrencySerializer(serializers.ModelSerializer):

    name = serializers.CharField()
    rate = serializers.DecimalField(max_digits=10, decimal_places=4)

    class Meta:
        model = Currency
        fields = [
            'id', 'name', 'rate'
        ]