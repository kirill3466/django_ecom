from django.contrib.auth.models import User
from django.test import TestCase

from .models import Category, Product, Review


class CategoryModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            name='Electronics', slug='electronics'
        )

    def test_category_creation(self):
        self.assertTrue(isinstance(self.category, Category))

    def test_category_str(self):
        self.assertEqual(str(self.category), 'Electronics')

    def test_category_ordering(self):
        self.assertEqual(Category._meta.ordering, ('name',))


class ProductModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            name='Electronics', slug='electronics'
        )
        self.product = Product.objects.create(
            category=self.category,
            name='Laptop',
            slug='laptop',
            description='Portable computer',
            price=100000,
        )

    def test_product_creation(self):
        self.assertTrue(isinstance(self.product, Product))

    def test_product_str(self):
        self.assertEqual(str(self.product), 'Laptop')

    def test_get_display_price(self):
        self.assertEqual(self.product.get_display_price(), 1000.00)

    def test_get_thumbnail_without_image(self):
        self.assertEqual(
            self.product.get_thumbnail(),
            'https://via.placeholder.com/240x240.jpg'
        )

    def test_get_thumbnail_with_image(self):
        pass

    def test_product_ordering(self):
        self.assertEqual(Product._meta.ordering, ('-created_at',))


class ReviewModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            'testuser', 'test@example.com', 'password'
        )
        self.category = Category.objects.create(
            name='Electronics', slug='electronics'
        )
        self.product = Product.objects.create(
            category=self.category,
            name='Laptop',
            slug='laptop',
            description='Portable computer',
            price=100000,
        )
        self.review = Review.objects.create(
            product=self.product,
            rating=5,
            content='Great product!',
            created_by=self.user,
        )

    def test_review_creation(self):
        self.assertTrue(isinstance(self.review, Review))

    def test_get_rating(self):
        # Assuming this is the only review for the product
        self.assertEqual(self.product.get_rating(), 5)

    def test_review_default_rating(self):
        new_review = Review.objects.create(
            product=self.product,
            content='Decent product.',
            created_by=self.user,
        )
        self.assertEqual(new_review.rating, 3)
