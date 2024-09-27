from rest_framework import serializers
from .models import DbAllStocks

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = DbAllStocks
        fields = ['id', 'title', 'author', 'description']