from django.urls import path
from .views import *

urlpatterns =[
    path("",home,name='home'),
    path("admin_dash/",admin_dash,name='admin'),
    path('delete/<int:id>/',delete,name='delete'),
    path('edit/<int:id>/',edit,name='edit'),
    path('aval/',aval,name='aval'),
    path('book/<int:id>/',book,name='book'),
    path('search/',search,name='search')
]