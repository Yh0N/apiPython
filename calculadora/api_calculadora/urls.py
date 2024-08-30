from django.urls import path
from .views import SumaView, RestaView, MultiplicacionView, DivisionView

urlpatterns = [
    path ('sumar', SumaView.as_view()),
    path ('restar', RestaView.as_view()),
    path ('multiplicar', MultiplicacionView.as_view() ),
    path ('dividir', DivisionView.as_view())
]
