from django.core.serializers import serialize
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render
from django.views.generic import View

from grupo.models import Grupo
from subgrupo.models import SubGrupo
from tarefa.models import Tarefa


class Index(LoginRequiredMixin, View):

    def get(self, request):

        grupos = Grupo.objects.all()

        return render(request, "home/index.html", {'grupos': grupos})

def get_subgrupos(request, id_grupo):

    if request.method == 'GET':
        grupo = get_object_or_404(Grupo, id=id_grupo)
        subgrupos = list(grupo.subgrupo_set.all().values('id', 'nome'))
        
        return JsonResponse({'subgrupos': subgrupos})   


def get_tarefas(request, id_subgrupo):

    if request.method == 'GET':
        subgrupo = get_object_or_404(SubGrupo, id=id_subgrupo)
        tarefas = list(subgrupo.tarefa_set.all().values('id', 'title'))
        
        return JsonResponse({'tarefas': tarefas})  
        

class Grupos(LoginRequiredMixin, View):

    def get(self, request):
        busca = request.GET.get('busca', '')
        grupos = Grupo.objects.filter(user=request.user)
        if busca:
            grupos = grupos.filter(nome__icontains=busca)

        context = {'grupos': grupos, 'busca': busca}

        return render(request, "home/grupos.html", context)


class SubGrupos(LoginRequiredMixin, View):

    def get(self, request):
        busca = request.GET.get('busca', '')
        subgrupos = SubGrupo.objects.filter(user=request.user)
        if busca:
            subgrupos = subgrupos.filter(nome__icontains=busca)

        context = {'subgrupos': subgrupos, 'busca': busca}

        return render(request, "home/subgrupos.html", context)


class Tarefas(LoginRequiredMixin, View):

    def get(self, request):
        busca = request.GET.get('busca', '')
        tarefas = Tarefa.objects.filter(user=request.user)
        if busca:
            tarefas = tarefas.filter(nome__icontains=busca)

        context = {'tarefas': tarefas, 'busca': busca}

        return render(request, "home/tarefas.html", context)