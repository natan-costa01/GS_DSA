
let passos = [];
let indice = 0;

const el = id => document.getElementById(id);


// ==========================================
// EXECUTAR FUNÇÕES DOS BOTÕES
// ==========================================

async function acao(nome) {

    if (
        ["excluir", "limpar"].includes(nome) &&
        !confirm("Confirma a operação?")
    ) {
        return;
    }

    const dados = {};

    const campos = [
        "id",
        "titulo",
        "categoria",
        "descricao",
        "requisitos",
        "local",
        "busca"
    ];

    for (const campo of campos) {

        dados[campo] = el(campo).value;

    }

    el("demo").hidden = true;

    try {

        const resposta = await fetch("/acao/" + nome, {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify(dados)

        });

        const resultado = await resposta.json();

        el("saida").replaceChildren();

        // Tratamento de erros

        if (!resposta.ok) {

            el("saida").textContent = resultado.erro;

            return;

        }

        // Análise dos registros

        if (resultado.analise) {

            const categorias = Object.entries(
                resultado.analise.categorias
            );

            el("saida").textContent =
                "Total: " + resultado.analise.total +
                " | " +
                categorias.map(
                    ([categoria, quantidade]) =>
                        categoria + ": " + quantidade
                ).join(" | ");

            return;

        }

        // Demonstração da ordenação

        if (resultado.passos) {

            passos = resultado.passos;

            indice = 0;

            el("demo").hidden = false;

            passo(0);

        }

        // Mostrar os serviços

        const registros = resultado.registros;

        if (registros.length) {

            el("saida").textContent =
                "IDs: " +
                registros.map(s => s.id).join(" → ") +
                " → null";

        } else {

            el("saida").textContent =
                "Nenhum serviço encontrado";

        }

        for (const servico of registros) {

            const artigo = document.createElement("article");

            artigo.textContent =
                `${servico.id} | ${servico.titulo} | ${servico.categoria}
${servico.descricao}
Requisitos: ${servico.requisitos}
Local: ${servico.local}`;

            el("saida").appendChild(artigo);

        }

        // Preencher campos após consultar ID

        if (nome === "consultar" && registros.length) {

            const campos = [
                "id",
                "titulo",
                "categoria",
                "descricao",
                "requisitos",
                "local"
            ];

            for (const campo of campos) {

                el(campo).value = registros[0][campo];

            }

        }

    } catch (erro) {

        el("saida").textContent =
            "Falha na comunicação com o backend.";

    }

}


// ==========================================
// DEMONSTRAÇÃO PASSO A PASSO
// ==========================================

function passo(delta) {

    indice = Math.max(
        0,
        Math.min(passos.length - 1, indice + delta)
    );

    const p = passos[indice];

    el("etapa").textContent =
        `${indice + 1}/${passos.length} — ${p.texto}`;

    el("sequencia").replaceChildren();

    for (const id of p.ids) {

        const span = document.createElement("span");

        span.textContent = id;

        el("sequencia").appendChild(span);

    }

    el("metricas").textContent =
        Object.entries(p.metricas)
            .map(([chave, valor]) => chave + ": " + valor)
            .join(" | ");

}


// Mostrar lista ao carregar a página

acao("listar");
