from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("bemerkung/<int:pk>", views.bemerkung, name='bemerkung'),
    path('bilder/<int:pk>', views.bilder, name='bilder'),
]