from django.urls import path
from .views import product_list, product_create, product_edit, product_delete

urlpatterns = [
    path("", product_list, name="product_list"),
    path("nuevo/", product_create, name="product_create"),
    path("editar/<int:pk>/", product_edit, name="product_edit"),
    path("borrar/<int:pk>/", product_delete, name="product_delete"),
]