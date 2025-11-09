from django.urls import path
from . import views

urlpatterns = [
    path('', views.restaurant_view, name='restaurant_view'),
    path('confirmacao/', views.reservation_confirmation, name='reservation_confirmation'),
    path('salvar/', views.salvar, name='salvar'),
    path('deletar_reserva/<int:reserva_id>/', views.deletar_reserva, name='deletar_reserva'),
    path('reservas/<int:reserva_id>/editar/', views.editar_reserva, name='editar_reserva'),
    path('formulario/', views.formulario_view, name='formulario_view'),
    
]
