from django.conf.urls import url

from . import views


urlpatterns = [

    url(r'^$', views.ProductsList.as_view(), name='products_list'),
    url(r'^(?P<product_pk>\d+)/$', views.ProductDetails.as_view(), name='product_detail'),

]
