import random

from models.servico import Servico
from structures.lista import ListaEncadeada
from algoritmos.busca import buscar_id, buscar_texto
from algoritmos.ordenacao import executar


lista = ListaEncadeada()

CATEGORIAS = [
    "RG",
    "CPF",
    "CNH",
    "Assistência Social"
]


# ==========================================
# CADASTRAR SERVIÇO
# ==========================================

def cadastrar_servico(dados):

    campos = [
        "titulo",
        "categoria",
        "descricao",
        "requisitos",
        "local"
    ]

    for campo in campos:

        if not isinstance(dados.get(campo), str):

            raise ValueError("Preencha todos os campos")

        if not dados[campo].strip():

            raise ValueError("Preencha todos os campos")

    if dados["categoria"] not in CATEGORIAS:

        raise ValueError("Categoria inválida")

    if len(lista.listar()) >= 9000:

        raise ValueError("Limite de IDs atingido")

    id = random.randint(1000, 9999)

    while buscar_id(lista, id) is not None:

        id = random.randint(1000, 9999)

    servico = Servico(
        id,
        dados["titulo"].strip(),
        dados["categoria"].strip(),
        dados["descricao"].strip(),
        dados["requisitos"].strip(),
        dados["local"].strip()
    )

    lista.inserir(servico)

    return servico


# ==========================================
# MOSTRAR LISTA
# ==========================================

def mostrar_lista():

    return lista.listar()


# ==========================================
# PESQUISAR ID
# ==========================================

def pesquisar_id(id):

    servico = buscar_id(lista, id)

    if servico is None:

        raise ValueError("ID não encontrado")

    return servico


# ==========================================
# BUSCAR TÍTULO
# ==========================================

def buscar_titulo(texto):

    return buscar_texto(lista, "titulo", texto)


# ==========================================
# BUSCAR CATEGORIA
# ==========================================

def buscar_categoria(texto):

    return buscar_texto(lista, "categoria", texto)


# ==========================================
# ATUALIZAR SERVIÇO
# ==========================================

def atualizar(id, dados):

    servico = pesquisar_id(id)

    campos = [
        "titulo",
        "categoria",
        "descricao",
        "requisitos",
        "local"
    ]

    for campo in campos:

        if not isinstance(dados.get(campo), str):

            raise ValueError("Preencha todos os campos")

        if not dados[campo].strip():

            raise ValueError("Preencha todos os campos")

    if dados["categoria"] not in CATEGORIAS:

        raise ValueError("Categoria inválida")

    for campo in campos:

        setattr(servico, campo, dados[campo].strip())

    return servico


# ==========================================
# EXCLUIR SERVIÇO
# ==========================================

def excluir(id):

    if not lista.remover(id):

        raise ValueError("ID não encontrado")


# ==========================================
# GERAR SERVIÇOS ALEATÓRIOS
# ==========================================

def gerar():

    for i in range(5):

        categoria = random.choice(CATEGORIAS)

        dados = {
            "titulo": f"Serviço fictício {categoria} {i + 1}",
            "categoria": categoria,
            "descricao": "Exemplo para teste",
            "requisitos": "Dados fictícios",
            "local": "Local fictício"
        }

        cadastrar_servico(dados)


# ==========================================
# ANALISAR REGISTROS
# ==========================================

def analisar():

    contagem = {}

    for servico in lista.listar():

        categoria = servico.categoria

        contagem[categoria] = contagem.get(categoria, 0) + 1

    return {
        "total": sum(contagem.values()),
        "categorias": contagem
    }


# ==========================================
# ORDENAR SERVIÇOS
# ==========================================

def ordenar(nome):

    return executar(nome, lista.listar())
