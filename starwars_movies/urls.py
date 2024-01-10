from django.urls import path
from .views import *


urlpatterns = [
    path('', starwars_data, name='starwars_data'),
    ]