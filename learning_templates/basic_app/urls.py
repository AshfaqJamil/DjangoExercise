from django.urls import path
from basic_app import views


#TEMPLATE TAGGING
app_name = 'basic_app'

urlpatterns=[
    path('relative/', views.relative, name='realtive' ),
    path('other/', views.other, name='other'),
]