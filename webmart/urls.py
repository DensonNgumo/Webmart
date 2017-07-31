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
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from mart_admin import views as adminViews
from customer_mart import views as customerViews
from cart import views as cartViews

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^add_products/$',adminViews.addProducts,name='add_products'),
    url(r'^add_categories/$',adminViews.addCategories,name='add_categories'),
    url(r'^$',customerViews.index,name='home'),
    url(r'^products/cat=/(?P<category_id>[0-9]+)/$',customerViews.productsByCategory,name='select_products'),
    url(r'^test/(?P<product_id>[0-9]+)/$',customerViews.addToCart,name='test'),
    url(r'^test/$',customerViews.test,name='testPage'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)