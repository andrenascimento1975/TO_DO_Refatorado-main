from django.urls import path

from .views import Index, get_subgrupos, get_tarefas, Grupos, SubGrupos, Tarefas


app_name = 'home'

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('get/subgrupos/<int:id_grupo>', get_subgrupos),
    path('get/tarefas/<int:id_subgrupo>', get_tarefas),
    path('grupos/', Grupos.as_view(), name='grupos'),
    path('subgrupos/', SubGrupos.as_view(), name='subgrupos'),
    path('tarefas/', Tarefas.as_view(), name='tarefas'),
]
