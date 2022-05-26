from django.urls import path

from contas.ui import categoria_views, transacao_views

urlpatterns = [
    # Tudo começa aqui, Taísa, onde nós declaramos as URLs(rotas) das nossas páginas customizadas. Como você já deve
    # imaginar, existem formas mais avançadas de se declarar essas rotas, porém nós vamos começar com o básico primeiro
    path('categorias/', categoria_views.list_categoria),
    path('categorias/novo/', categoria_views.create_categoria),
    path('categorias/<categoria_id>/', categoria_views.update_caregoria),
    path('categorias/<categoria_id>/delete/', categoria_views.delete_categoria),
    path('transacoes/', transacao_views.TransacaoView.as_view(), name='list'),

    # Como prometido, aqui tem uma forma um pouco menos verbosa de declarar as rotas, mas isso aumento o trabalho lá na
    # view
    path(r'transacoes/<transacao_id>/', transacao_views.TransacaoView.as_view()),
    path(r'transacoes/<transacao_id>/<delete>/', transacao_views.TransacaoView.as_view()),
]
