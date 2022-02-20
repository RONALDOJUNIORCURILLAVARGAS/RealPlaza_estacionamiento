from . import views
from django.urls import path

urlpatterns = [
    path('',views.index,name='inicio'),  
    path('salir/',views.salir, name="salir"),
    path('reserve/',views.reservas,name='page-reserve'),
    path('reserve/reg/',views.reg_reserve, name='reg-reserve'),
    path('sedes/',views.sedes,name='sedes'),
    # path('',bienvenido,name='inicio'),

]
