from django.urls import include, path
from rest_framework import routers, urlpatterns
from . import views

from .views import ProductList

router = routers.DefaultRouter()

# All products, no filter
# 12 products per page
router.register(r'products', views.ProductViewSet)

# Products grouped by category, no filter
# 1 category per page
router.register(r'groups', views.GroupViewSet)

# All categories of products
router.register(r'categories', views.CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    
    # 12 products per page
    # Regex search
    path('list/', ProductList.as_view(), name='postsearch'),
    # + Filter by category
    # + Order by category id, name, price
    # Example of use: 
    # http://hosturl/list/1/?page=1&search=&ordering=category_id
    
    path('list/<int:category_id>/', ProductList.as_view()),
]