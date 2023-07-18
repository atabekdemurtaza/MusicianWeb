from django.urls import path
from .views import (
    about,
    sale,
    repairs,
    create,
    home,
    sale_detail
)

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('sale/', sale, name='sale'),
    path('sale/<pk>/', sale_detail, name='sale_detail'),
    path('repairs/', repairs, name='repairs'),
    path('create/', create, name='create'),
]

