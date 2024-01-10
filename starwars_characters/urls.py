from django.urls import path
from .views import *


urlpatterns = [
    path('characters', starwars_data, name='starwars_data'),
    ]