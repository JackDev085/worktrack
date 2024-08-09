from django.contrib import admin
from django.urls import path
from workouts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('pesquisa', views.pesquisa, name='pesquisa'),
    path('exercicio/<int:id>', views.exercicio, name='exercicio'),
]
