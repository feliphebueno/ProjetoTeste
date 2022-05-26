from django.http import HttpResponseRedirect, HttpRequest
from django.shortcuts import render
from django.views import View

from contas.models import Categoria, Transacao
from contas.ui.forms import TransacaoForm


class TransacaoView(View):
    """
    Aqui a nossa view é uma classe, ao invés de funções 'jogadas' no arquivo, isso ajuda a agrupar recursos similares,
    como nesse caso, onde tudo aqui está relecionado a Transações.
    """
    form_class = TransacaoForm
    template_name = 'ui/transacoes/list_table.html'

    def get(self, request: HttpRequest, *args, **kwargs):
        """
        Requisições GET são recebidas aqui
        """
        return self.router(request, *args, **kwargs)

    def post(self, request: HttpRequest, *args, **kwargs):
        """
        Requisições POST são recebidas aqui
        """
        return self.router(request, *args, **kwargs)

    def router(self, request: HttpRequest, *args, **kwargs):
        """
        Este método é responsável por determinar qual método irá responder a requisição, de acordo com os parâmetros na
        URL
        """
        transacao_id = kwargs['transacao_id'] if 'transacao_id' in kwargs else None
        delete = True if 'delete' in kwargs else False

        if transacao_id == 'novo':  # Create
            return self.create_transacao(request)
        else:
            if transacao_id and not delete:  # Update
                return self.update_transacao(request, transacao_id)
            elif transacao_id and delete:  # Delete
                return self.delete_transacao(request, transacao_id)
            else:  # Read
                return self.list_transacoes(request)

    # Daqui pra baixo são basicamente os mesmos métodos da outra view(categorias)
    def create_transacao(self, request: HttpRequest):
        context = {}
        form = self.form_class(request.POST or None)
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/transacoes/')  # Retorna pra lista geral

        context['form'] = form
        return render(request, "ui/transacoes/form_template.html", context)

    def list_transacoes(self, request: HttpRequest):
        transacoes = Transacao.objects.all()

        return render(request, self.template_name, {'transacoes': transacoes})

    def update_transacao(self, request: HttpRequest, transacao_id: int):
        context = {}
        transacao = Transacao.objects.filter(id=transacao_id).first()

        if request.method == 'POST':
            form = self.form_class(request.POST, instance=transacao)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/transacoes/')
        else:
            form = self.form_class({
                **transacao.__dict__,
                **{'categoria': transacao.categoria_id}
            })
        print(form.data['observacoes'])
        context['form'] = form
        return render(request, "ui/transacoes/form_template.html", context)

    def delete_transacao(self, request: HttpRequest, transacao_id: int):
        transacao = Transacao.objects.filter(id=transacao_id).first()

        if request.method == 'POST' and transacao:
            transacao.delete()
            return HttpResponseRedirect('/transacoes/')

        context = {
            'id': transacao.id,
            'descricao': transacao.descricao
        }

        return render(request, 'ui/transacoes/delete_form_template.html', {'transacao': context})
