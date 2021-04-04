from django.urls import path
from django.conf import settings 
from django.conf.urls.static import static 
from .views import (products,buyProduct,about,allOrders,deleteOrder,
    allEmployee,addEmployee,deleteEmployee,takeAttendence)

urlpatterns=[
    path('products/',products,name='products'),
    path('buy_product/<int:id>/',buyProduct,name='buy_product'),
    path('about_us/',about,name='about'),
    path('all_orders',allOrders,name='all_orders'),
    path('delete_order/<int:id>/',deleteOrder,name='delete_order'),
    path('all_employee/',allEmployee,name='all_employee'),
    path('add_employee',addEmployee,name='add_employee'),
    path('delete_employee/<int:id>/',deleteEmployee,name='delete_employee'),
    path('take_attendence/',takeAttendence,name='take_attendence')
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)