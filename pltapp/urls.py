from django.urls import path
from .views import index , updated 

urlpatterns = [
    path('', index , name='home'),
    path ('update/', updated , name='update' )
]
