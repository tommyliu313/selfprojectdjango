from django.urls import path, include
from . import views

urlpatterns = [
    path('<int:warehouse_id>', views.warehouse_one, name='warehouse'),
    path('',views.warehouse, name="warehouse"),
    path('<str:region_name>', views.show_region, name='region')
]
