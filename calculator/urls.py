from django.urls import path
from .views import home


urlpatterns = [
    path('',home),
    # path('result/',add),
    # path('result/',sub),
    # path('result/',multi),
    # path('result/',div),
]