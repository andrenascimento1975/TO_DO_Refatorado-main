from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Grupo


class VerGrupo(LoginRequiredMixin, GroupRequiredMixin, View):
    group_required = (u"Auditores", u"SGCE", u"Inspetores Gerais", u"Supervisores")

    def get(self, request, slug_grupo):
        busca = request.GET.get('busca', '')
        grupo = get_object_or_404(Grupo, slug=slug_grupo)
        subgrupos = grupo.subgrupo_set.all()

        if busca:
            subgrupos = subgrupos.filter(nome__icontains=busca)

        context = {'grupo': grupo, 'subgrupos': subgrupos, 'busca': busca}

        return render(request, "grupo/grupo.html", context)


class CriarGrupo(LoginRequiredMixin, GroupRequiredMixin, CreateView):
    group_required = u"SGCE"
    model = Grupo
    context_object_name = 'criar_grupo'
    success_url = reverse_lazy('home:index')
    fields = ('nome',)
    template_name = 'grupo/formulario_grupo.html'

    def dispatch(self, request, *args, **kwargs):
        self.request = request
        in_group = False
        if request.user.is_authenticated:
            in_group = self.check_membership(self.get_group_required())
            if not in_group:
                return self.handle_no_permission(request)
        return super(GroupRequiredMixin, self).dispatch(
                request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
            return super(CriarGrupo, self).form_valid(form)

class AtualizarGrupo(LoginRequiredMixin, GroupRequiredMixin, UpdateView):
    group_required = (u"SGCE", u"Inspetores Gerais", u"Supervisores")
    model = Grupo
    fields = '__all__'
    success_url = reverse_lazy('grupos')
    template_name = 'login/formulario_grupos.html'


class ApagarGrupo(LoginRequiredMixin, GroupRequiredMixin, DeleteView):
    group_required = (u"SGCE", u"Inspetores Gerais")
    model = Grupo
    fields = '__all__'
    success_url = reverse_lazy('grupos')
    template_name = 'login/apagar_grupo.html'
