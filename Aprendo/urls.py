"""Define los patrones para urls de aprendo."""

from django.urls import path, include
from . import views


urlpatterns = [
    # home page 
    path('',views.index, name='index'),
    #pagina que muestra los topics.
    path('topics/', views.topics, name='topics'),
    #pagina detallada para un solo topico
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    #pagina para adjuntar nuevos topicos temas 
    path('new_topic/', views.new_topic, name='new_topic'),
    #pagina para adjuntar nuevas entradas 
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    #pagina para editar un entry
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]
