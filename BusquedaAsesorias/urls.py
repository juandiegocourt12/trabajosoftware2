from django.urls import path

from . import views

urlpatterns = [
    path('BusquedaAsesorias/', BusquedaAsesoriasView.as_view(?filter=filter-val&orderby=order-val), name='BusquedaAsesorias'),
]
