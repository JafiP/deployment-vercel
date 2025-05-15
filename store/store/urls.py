"""store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from my_app.views import get_products, get_product,index,main,base,buy,ordering




urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',index , name='index'),
    path('ordering/',ordering , name='ordering'),
    path('buy/', buy , name='buy'),
    path('hello/',base , name='hello'),#
    path('shop/', main , name='shop' ),
    path('product/<int:id>/', get_product, name='product'),
    path('products/', get_products , name='products' ),
    path('products/<int:category_id>', get_products , name='products_id' ),
    
]
