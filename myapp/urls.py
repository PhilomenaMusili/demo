from django.urls import path
from . import views

urlpatterns = [
    path("",views.home, name="home"),
    path("todos/",views.todos, name="Todos"),
    path('contact/', views.contact_view, name='contact'),
    path('contact/update/<int:pk>/', views.update_contact, name='update_contact'),
]
