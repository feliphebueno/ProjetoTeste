"""
Neste module(arquivo) nós iremos definir os forms que os nossos usuários utilizaram para submeter dados para a nossa
APP, ligeiramente parecido com o que o admin já faz, porém aqui o nosso formulário vai ficar em uma interface
completamente nossa, então nós podemos customizá-la de acordo com a nossa vontade e/ou necessidade. Porém, a parte chata
de lidar com formulário(input do usuário) essa classe forms.ModelForm faz pra nós e acredite, isso é uma mão-na-roda,
no OnyxPrev não temos essa colher-de-chá e às vezes fazer uma tela simples com 2 ou 3 campos pode acabar com o seu dia.
"""
from django import forms
from contas.models import Categoria, Transacao


class CategoriaForm(forms.ModelForm):
    """
    Esse, obviamente é o formulário que vai preencher o model Categoria, muito coisa é automatizada, não tem problema,
    frameworks existem pra isso mesmo: pra nós utilizarmos "códigos dos outros" pra facilitar a nossa vida ;)
    """
    class Meta:
        # Aqui você informa o model
        model = Categoria

        # Aqui você define quais campos deste model você quer permitir que sejam atualizados através deste form
        fields = [
            'nome',
        ]


class TransacaoForm(forms.ModelForm):
    """
    Esse é o formulário que vai preencher o model Transacao
    """
    class Meta:
        # Aqui você informa o model
        model = Transacao

        # Aqui você define quais campos deste model você quer permitir que sejam atualizados através deste form
        fields = [
            'descricao',
            'valor',
            'categoria',
            'observacoes',
            'data'
        ]
