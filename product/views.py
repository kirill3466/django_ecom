from django.shortcuts import get_object_or_404, redirect, render
from django.views import View

from .models import Product, Review


class ProductView(View):
    def get(self, request, slug):
        product = get_object_or_404(Product, slug=slug)
        return render(request, 'product/product.html', {'product': product})

    def post(self, request, slug):
        product = get_object_or_404(Product, slug=slug)
        rating = request.POST.get('rating', 3)
        content = request.POST.get('content', '')

        if content:
            reviews = Review.objects.filter(
                created_by=request.user, product=product
            )

            if reviews.count() > 0:
                review = reviews.first()
                review.rating = rating
                review.content = content
                review.save()
            else:
                review = Review.objects.create(
                    product=product,
                    rating=rating,
                    content=content,
                    created_by=request.user
                )

            return redirect('product', slug=slug)

        return render(request, 'product/product.html', {'product': product})
