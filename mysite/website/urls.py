from django.urls import path
from .views import *
from website import views
#
app_name='website'
urlpatterns = [
    
    path('', home, name = 'homepage'),
    path('sendmail/', send_gmail, name = 'sendmail'),
    path('laptops/', laptops, name = 'laptops'),
    path('pcs/', pcs, name = 'pcs'),
    path('aboutus/', about, name = 'about'),
    path('contact/', contact, name = 'contact'),
    path('accessories/', accessories, name = 'accessories'),
    path('phone/', phone, name = 'phone'),
    path('products/', product, name = 'product'),
    path('service/', service, name = 'service'),
    path('portfolio-details/', portfolio, name = 'portfolio'),
    path('contact/', contactpage, name = 'contactpage'),

    path('contacting/', ContactView.as_view(), name="contacting"),
    path('success/', ContactSuccessView.as_view(), name="success"),
   
]