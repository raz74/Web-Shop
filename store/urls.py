from django.urls import path
from . import views

# URLconfig
urlpatterns = [
    path('', views.homepage),
    path('product/', views.product_list),

]
