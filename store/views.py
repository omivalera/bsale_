from django.shortcuts import render
from rest_framework import viewsets, pagination, generics, filters

from .serializers import CategorySerializer, ProductSerializer, GroupSerializer
from .models import Product, Category

class GroupPagination(pagination.PageNumberPagination):
    page_size = 1

class ProductPagination(pagination.PageNumberPagination):
    page_size = 12

class ProductViewSet(viewsets.ModelViewSet):
    '''
    List of products: 
    - 12 products per page
    '''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductPagination

class ProductList(generics.ListAPIView):
    '''
    List of products: 
    - 12 products per page
    - Regex search in product
    - Filter by category
    - Order by name, price, category_id
    '''
    model = Product
    pagination_class = ProductPagination
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['$name']
    ordering_fields = ['name', 'price', 'category_id']

    def get_queryset(self):
        try:
            cat_id = int(self.kwargs['category_id'])
            return Product.objects.filter(category_id = cat_id)
        except:
            return Product.objects.all()

class GroupViewSet(viewsets.ModelViewSet):
    '''
    List of products grouped by category: 
    - 1 category per page
    - Regex search in category
    '''
    queryset = Category.objects.all()
    serializer_class = GroupSerializer
    pagination_class = GroupPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['$name']

class CategoryViewSet(viewsets.ModelViewSet):
    '''
    List of all categories of products
    '''
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
