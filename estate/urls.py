from django.urls import path

from estate import views

app_name = 'estate'

urlpatterns = [
    path('', views.immovable_list, name='immovable_list'),
    path('holders/', views.holder_list, name='holder_list'),
    path('realtors/', views.realtor_list, name='realtor_list')
]
