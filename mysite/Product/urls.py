from django.urls import path
from . import AdminView
from . import views
app_name='Product'
urlpatterns = [
    path('pro', views.ShowAllProducts, name='showProducts'),
    path('customerShow', views.ShowAllProduct, name='showProduct'),
    path('product/<int:pk>/', views.productDetail, name='product'),
    path('addProduct/', views.addProduct, name='addProduct'),
    path('updateProduct/<int:pk>/', views.updateProduct, name='updateProduct'),
    path('deleteProduct/<int:pk>/', views.deleteProduct, name='deleteProduct'),
    path('search/', views.searchBar, name='search'),
    path('product/<int:pk>/add-comment', views.add_comment, name='add-comment'),
    path('product/<int:pk>/delete-comment', views.delete_comment, name='delete-comment'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('doLogin',views.doLogin,name="dologin"),
    path('logout', views.logout, name='logout'),
    path('logout_view', views.logout_view, name='logout_view'),
    path('add_staff',AdminView.add_staff,name="add_staff"),
    path('add_staff_save',AdminView.add_staff_save,name="add_staff_save"),
]