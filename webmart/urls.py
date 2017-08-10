"""webmart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from mart_admin import views as adminViews
from customer_mart import views as customerViews
from cart import views as cartViews

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^add_products/$',adminViews.addProducts,name='add_products'),
    url(r'^add_categories/$',adminViews.addCategories,name='add_categories'),
    url(r'^$',customerViews.index,name='home'),
    url(r'^details/(?P<product_id>[0-9]+)/$',customerViews.details,name='details'),
    url(r'^products/cat=/(?P<category_id>[0-9]+)/$',customerViews.productsByCategory,name='select_products'),
    url(r'^cart/add/(?P<product_id>[0-9]+)/$',cartViews.addToCart,name='add_to_cart'),
    url(r'^cart/remove/(?P<product_id>[0-9]+)/$',cartViews.removeFromCart,name='remove_from_cart'),
    url(r'^cart/$',cartViews.loadCart,name='cart_items'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)