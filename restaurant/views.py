from django.db.models import Prefetch
from rest_framework.response import Response
from rest_framework.views import APIView

from restaurant.models import Food, FoodCategory
from restaurant.serializers import FoodListSerializer


class FoodCategories(APIView):
    def get(self, request):
        published_foods = Food.objects.filter(is_publish=True)
        categories_with_foods = FoodCategory.objects.prefetch_related(
            Prefetch('food', queryset=published_foods)
        ).distinct()
        serializer = FoodListSerializer(categories_with_foods, many=True)
        return Response(serializer.data)
