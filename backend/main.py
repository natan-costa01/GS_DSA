
from flask import Flask, request, jsonify, send_from_directory
from pathlib import Path
from dataclasses import asdict

from services import gerenciamento as g


app = Flask(__name__)

frontend = Path(__file__).resolve().parent.parent / "frontend"


@app.get("/")
def home():

    return send_from_directory(frontend, "index.html")


@app.get("/assets/<path:nome>")
def assets(nome):

    return send_from_directory(frontend, nome)


@app.post("/acao/<acao>")
def acao(acao):

    dados = request.get_json(silent=True) or {}

    try:

        if acao == "cadastrar":

            g.cadastrar_servico(dados)

        elif acao == "consultar":

            servico = g.pesquisar_id(int(dados["id"]))

            return jsonify(registros=[asdict(servico)])

        elif acao in ("titulo", "categoria"):

            texto = dados.get("busca", "").strip()

            if not texto:

                raise ValueError("Digite o termo da busca")

            if acao == "titulo":

                resultado = g.buscar_titulo(texto)

            else:

                resultado = g.buscar_categoria(texto)

            return jsonify(
                registros=[asdict(s) for s in resultado]
            )

        elif acao == "atualizar":

            g.atualizar(int(dados["id"]), dados)

        elif acao == "excluir":

            g.excluir(int(dados["id"]))

        elif acao == "gerar":

            g.gerar()

        elif acao == "analisar":

            return jsonify(analise=g.analisar())

        elif acao in ("bubble", "merge", "tree"):

            registros, metricas, passos = g.ordenar(acao)

            return jsonify(
                registros=[asdict(s) for s in registros],
                metricas=metricas,
                passos=passos
            )

        elif acao == "limpar":

            g.lista.inicio = None
            g.lista.ultimo = None

        elif acao != "listar":

            raise ValueError("Opção inválida")

        return jsonify(
            registros=[asdict(s) for s in g.mostrar_lista()]
        )

    except (ValueError, KeyError, TypeError) as erro:

        return jsonify(erro=str(erro)), 400


if __name__ == "__main__":

    app.run(port=5000)
