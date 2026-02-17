from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('test/', views.pagina_test, name='pagina_test'),
    path('rezultate/', views.pagina_rezultate, name='pagina_rezultate'),
]