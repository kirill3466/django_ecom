from django.db.models import Avg, Count, F, Max, Min, Sum
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from product.models import Product
from product.serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all()
        return queryset

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response.data.append(self.stats())
        return response

    @staticmethod
    def top_product():
        top_product_id = Product.objects.annotate(
            total_rating=Sum('reviews__rating')
        ).order_by('-total_rating').first().id
        return top_product_id

    def stats(self, *args, **kwargs):
        if not Product.objects.exists():
            return None
        avg_price = Product.objects.aggregate(avg_price=Avg('price'))
        count = Product.objects.count()
        min_max_price = Product.objects.aggregate(
            min_price=Min('price'),
            max_price=Max('price')
        )
        highly_rated = Product.objects.filter(reviews__rating__gte=4).annotate(
            avg_rating=Avg('reviews__rating'),
            count_reviews=Count('reviews__id')
        ).values('id', 'avg_rating', 'count_reviews')
        # update_test = Product.objects.update(price=F('price') + 1)
        return {
            'stats': {
                'avg_price': avg_price['avg_price'],
                'count': count,
                'price': min_max_price,
                'highly_rated': highly_rated,
                'top_product_id': self.top_product(),
            }
        }


@api_view(['GET'])
def test(request):
    product = Product.objects.get(pk=1)
    serializer = ProductSerializer(product)
    return Response(serializer.data, status=200)
