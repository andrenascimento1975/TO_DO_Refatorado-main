from django.urls import path, include
from .views import VerGrupo, CriarGrupo, AtualizarGrupo, ApagarGrupo
from django.contrib import admin

app_name = 'grupo'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('grupo/criar/', CriarGrupo.as_view(), name='criar'),
    path('<slug_grupo>/', VerGrupo.as_view(), name='grupo'),
    path('<slug_grupo>/atualizar/', AtualizarGrupo.as_view(), name='atualizar'),
    path('<slug_grupo>/apagar/', ApagarGrupo.as_view(), name='apagar'),
]
