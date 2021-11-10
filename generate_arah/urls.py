from django.urls import path
from .views import (
    home,
)

appname = "generate_arah"

urlpatterns = [
    path('', home, name='home'),
]
