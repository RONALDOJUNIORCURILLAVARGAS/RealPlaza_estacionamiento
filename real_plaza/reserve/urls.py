
from . import views
from django.urls import path

urlpatterns = [
    path('',views.index,name='inicio'),  
    path('salir/',views.salir, name="salir"),
    path('reserve/',views.reservas,name='page-reserve'),
    path('reserve/reg/',views.reg_reserve, name='reg-reserve'),
    path('reserve/reg/<int:id>',views.reg_reserve_sede,name='reg-reserve-sede'),
    path('sedes/',views.sedes,name='sedes'),
    path('registro/',views.RegistrarUsuario.as_view(),name='registrar'),
    path('reserve/historialreserve/',views.Verhistorial,name='historial-reservas'),
    path('reserve/reg/reservar/',views.estacionar,name='selecccionar-estacionamiento'),
    path('reserve/reg/reservar/payment/',views.Pagos.as_view(),name='pagar'),
    
    # path('',bienvenido,name='inicio'),

]
