def buscar_id(lista, id):

    atual = lista.inicio

    while atual is not None:

        if atual.servico.id == id:
            return atual.servico

        atual = atual.proximo

    return None


def buscar_texto(lista, campo, texto):

    resultado = []
    atual = lista.inicio

    while atual is not None:

        valor = getattr(atual.servico, campo)

        if texto.casefold() in valor.casefold():

            resultado.append(atual.servico)

        atual = atual.proximo

    return resultado
