from models.servico import Servico
from algoritmos.ordenacao import executar
from structures.lista import ListaEncadeada
from algoritmos.busca import buscar_id


algoritmos = [
    "bubble",
    "merge",
    "tree"
]

casos = [
    [50, 20, 80, 10, 30],
    [],
    [1],
    [1, 2, 3],
    [3, 2, 1]
]


# ==========================================
# TESTES DE ORDENAÇÃO
# ==========================================

for ids in casos:

    registros = []

    for id in ids:

        servico = Servico(
            id,
            str(id),
            "RG",
            "Teste",
            "Teste",
            "Teste"
        )

        registros.append(servico)

    for algoritmo in algoritmos:

        resultado, metricas, passos = executar(
            algoritmo,
            registros
        )

        saida = [s.id for s in resultado]

        assert saida == sorted(ids)

        print("\n===================================")

        print("Algoritmo:", algoritmo)
        print("Lista original:", ids)
        print("Lista ordenada:", saida)

        print("Comparações:", metricas["comparacoes"])
        print("Trocas:", metricas["trocas"])
        print("Movimentações:", metricas["movimentacoes"])
        print("Inserções:", metricas["insercoes"])

        print("Teste aprovado!")


# ==========================================
# TESTES DA LISTA ENCADEADA
# ==========================================

lista = ListaEncadeada()

for id in [3, 1, 2]:

    lista.inserir(
        Servico(
            id,
            str(id),
            "RG",
            "Teste",
            "Teste",
            "Teste"
        )
    )


assert buscar_id(lista, 1).id == 1

assert buscar_id(lista, 99) is None

assert lista.remover(3)

assert lista.remover(2)

assert lista.remover(1)

assert lista.inicio is None

assert lista.ultimo is None

assert not lista.remover(99)


print("\n===================================")
print("TODOS OS TESTES PASSARAM!")
print("===================================")
