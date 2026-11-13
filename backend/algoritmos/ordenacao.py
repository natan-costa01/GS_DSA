
from structures.arvore import NoArvore


def executar(nome, registros):

    dados = list(registros)

    metricas = {
        "comparacoes": 0,
        "trocas": 0,
        "movimentacoes": 0,
        "insercoes": 0
    }

    passos = []

    def registrar(texto, valores):

        passos.append({
            "texto": texto,
            "ids": [s.id for s in valores],
            "metricas": metricas.copy()
        })

    registrar("Sequência original", dados)

    # ==========================================
    # BUBBLE SORT
    # ==========================================

    if nome == "bubble":

        for i in range(len(dados) - 1):

            mudou = False

            for j in range(len(dados) - 1 - i):

                metricas["comparacoes"] += 1

                a = dados[j].id
                b = dados[j + 1].id

                if a > b:

                    dados[j], dados[j + 1] = (
                        dados[j + 1], dados[j]
                    )

                    metricas["trocas"] += 1

                    mudou = True

                    registrar(
                        f"Troca: {a} e {b}",
                        dados
                    )

                else:

                    registrar(
                        f"Comparação: {a} <= {b}",
                        dados
                    )

            if not mudou:
                break

    # ==========================================
    # MERGE SORT
    # ==========================================

    elif nome == "merge":

        def merge_sort(v):

            if len(v) <= 1:
                return v

            meio = len(v) // 2

            registrar("Dividir bloco", v)

            esquerda = merge_sort(v[:meio])
            direita = merge_sort(v[meio:])

            resultado = []

            i = 0
            j = 0

            while i < len(esquerda) and j < len(direita):

                metricas["comparacoes"] += 1

                if esquerda[i].id <= direita[j].id:

                    resultado.append(esquerda[i])
                    i += 1

                else:

                    resultado.append(direita[j])
                    j += 1

                metricas["movimentacoes"] += 1

                registrar(
                    "Intercalar: adicionar menor ID",
                    resultado
                )

            for restante in (esquerda[i:], direita[j:]):

                for item in restante:

                    resultado.append(item)

                    metricas["movimentacoes"] += 1

                    registrar(
                        "Adicionar restante ao bloco",
                        resultado
                    )

            return resultado

        dados = merge_sort(dados)

    # ==========================================
    # TREE SORT - ÁRVORE BINÁRIA DE BUSCA
    # ==========================================

    elif nome == "tree":

        raiz = None
        inseridos = []

        for servico in dados:

            novo = NoArvore(servico)
            caminho = []

            if raiz is None:

                raiz = novo

            else:

                atual = raiz

                while True:

                    metricas["comparacoes"] += 1

                    caminho.append(str(atual.servico.id))

                    if servico.id < atual.servico.id:

                        lado = "esquerda"

                    else:

                        lado = "direita"

                    if getattr(atual, lado) is None:

                        setattr(atual, lado, novo)

                        caminho.append(lado)

                        break

                    atual = getattr(atual, lado)

            inseridos.append(servico)

            metricas["insercoes"] += 1

            registrar(
                f"Inserir {servico.id}: "
                + (" -> ".join(caminho) or "raiz"),
                inseridos
            )

        # Percurso em ordem da árvore

        dados = []
        pilha = []
        atual = raiz

        while atual is not None or pilha:

            while atual is not None:

                pilha.append(atual)
                atual = atual.esquerda

            atual = pilha.pop()

            dados.append(atual.servico)

            metricas["movimentacoes"] += 1

            registrar(
                f"Percurso em ordem: {atual.servico.id}",
                dados
            )

            atual = atual.direita

    else:

        raise ValueError("Algoritmo inválido")

    registrar("Ordenação concluída", dados)

    return dados, metricas, passos
