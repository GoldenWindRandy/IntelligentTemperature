from django.urls import path,include
from Product import views
from rest_framework.urlpatterns import format_suffix_patterns



urlpatterns = [
    # 作品
    path('product/', views.ProductList.as_view()),
    
    path('hotProduct/', views.get_hot),
    # 分类
    path('category/',views.CategoryList.as_view()),
    # 单独作品
    path('product/<int:pk>/', views.product_detail.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)