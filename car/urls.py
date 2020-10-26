from django.urls import path
from .views import CarFormView

app_name = 'car'

urlpatterns = [
    path('', CarFormView.as_view()),
]