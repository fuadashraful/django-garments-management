from django.urls import path
from django.conf import settings 
from django.conf.urls.static import static 
from .views import products,buyProduct,about

urlpatterns=[
    path('products/',products,name='products'),
    path('buy_product/<int:id>/',buyProduct,name='buy_product'),
     path('about_us',about,name='about'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)