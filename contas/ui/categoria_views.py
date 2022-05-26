from django.http import HttpResponseRedirect
from django.shortcuts import render

from contas.models import Categoria
from contas.ui.forms import CategoriaForm


def list_categoria(request):
    """
    Código back-end para a tela que LISTA as categorias
    :param request: HttpRequest
    :return: Any
    """
    # Coletamos todas as categorias do banco de dados, através do model
    # Essa estrutura da linha 17 à 23 se chama "List Comprehension", é bem legal, dá uma olhadinha aqui pra entender
    # melhor: https://medium.com/data-hackers/aprenda-list-comprehension-7335844265bd
    categorias = [
        {
            'id': cat.id,
            'nome': cat.nome,
            'dt_criacao': cat.dt_criacao.strftime("%d/%m/%Y")
        } for cat in Categoria.objects.all()
    ]

    return render(request, "ui/categorias/list_table.html", {'categorias': categorias, "text_slice_length": 5, "text": "FELIPHE-BUENO"})


def create_categoria(request):
    """
    Código back-end para a tela que CRIA uma categoria
    :param request: HttpRequest
    :return: Any
    """
    context = {}
    # Instância do form vazia, isso é, os campos limpos pro usuário criar um novo registro
    form = CategoriaForm(request.POST or None)
    if request.method == 'POST':  # Salvando um novo registro
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/categorias/')  # Retorna pra lista geral

    context['form'] = form
    return render(request, "ui/categorias/form_template.html", context)


def update_caregoria(request, **params):
    """
    Código back-end para a tela que ALTERA uma categoria
    :param request: HttpRequest
    :return: Any
    """
    context = {}
    categoria_id = params['categoria_id']
    categoria = Categoria.objects.filter(id=categoria_id).first()

    if request.method == 'POST':  # Salvando um registro existente atualizado
        # Instância do form com os dados atualizados pelo usuário
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():  # Se o usuário preencheu tudo certinho
            form.save()  # Salva no BD
            return HttpResponseRedirect('/categorias/')  # Retorna pra lista geral
    else:  # Listando para edição
        # Instância do form carregada, com os dados do registro já existente no banco para o usuário alterá-los
        form = CategoriaForm({'nome': categoria.nome})

    context['form'] = form
    return render(request, "ui/categorias/form_template.html", context)


def delete_categoria(request, **params):
    """
    Código back-end para a tela que DELETA uma categoria
    :param request: HttpRequest
    :return: Any
    """
    categoria_id = params['categoria_id']
    categoria = Categoria.objects.filter(id=categoria_id).first()

    if request.method == 'POST':  # Removendo o registro selecionado pelo usuário
        # não precisamos validar o form aqui, pois pra excluir só precisamos da id
        categoria.delete()  # Registro removido do BD, sem chances pra arrpendimento ;)
        return HttpResponseRedirect('/categorias/')  # Retorna pra lista geral

    context = {
        'id': categoria.id,
        'nome': categoria.nome
    }

    return render(request, "ui/categorias/delete_form_template.html", {'categoria': context})
