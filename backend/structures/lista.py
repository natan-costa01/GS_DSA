
from models.no import No


class ListaEncadeada:

    def __init__(self):
        self.inicio = None
        self.ultimo = None

    def inserir(self, servico):

        novo = No(servico)

        if self.inicio is None:
            self.inicio = novo

        else:
            self.ultimo.proximo = novo

        self.ultimo = novo

    def listar(self):

        resultado = []
        atual = self.inicio

        while atual is not None:

            resultado.append(atual.servico)
            atual = atual.proximo

        return resultado

    def remover(self, id):

        atual = self.inicio
        anterior = None

        while atual is not None:

            if atual.servico.id == id:

                if anterior is None:
                    self.inicio = atual.proximo

                else:
                    anterior.proximo = atual.proximo

                if atual is self.ultimo:
                    self.ultimo = anterior

                return True

            anterior = atual
            atual = atual.proximo

        return False
