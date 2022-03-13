from django.urls import include, path
from rest_framework import routers, urlpatterns
from . import views

from .views import ProductList

router = routers.DefaultRouter()

# All products, no filter


router.register(r'products', views.ProductViewSet)

# Products grouped by category, no filter
# 1 categoris por pagina
router.register(r'groups', views.GroupViewSet)

# Todas las cateogiras
router.register(r'categories', views.CategoryViewSet)
router.register(r'list', views.ProductViewSet)




urlpatterns = [
    path('', include(router.urls)),
    

    path('list/', ProductList.as_view(), name='postsearch'),

    
    path('list/<int:category_id>/', ProductList.as_view()),
]