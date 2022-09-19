
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home),

    path('setting',views.setting),
    path('add',views.add, name='add')
]
