
<div align="center">

# CITIZEN TECH

### Global Solution 2026.2 — FIAP

**Sistema de Gerenciamento de Serviços Públicos**

Data Structures and Algorithms (DSA)

Python • Flask • Lista Encadeada • Algoritmos de Busca e Ordenação

</div>

---
## Equipe de desenvolvimento

Projeto desenvolvido por estudantes da FIAP para a disciplina de Data Structures and Algorithms.

| Integrante | RM |
|---|---|
| Leonardo Scotti Tobias | 573305 |
| Natan Silva da Costa | 573100 |
| Henrique de Souza Aragão | 570529 |

---

## 1. Sobre o projeto

O **Citizen Tech** é um projeto acadêmico desenvolvido para a **Global Solution 2026.2 — Citizen Tech da FIAP**, na disciplina de **Data Structures and Algorithms (DSA)**.

O sistema foi desenvolvido para organizar e gerenciar informações sobre serviços públicos, utilizando estruturas de dados e algoritmos implementados em Python.

A proposta permite realizar operações de cadastro, consulta, atualização, exclusão, pesquisa e ordenação de registros, demonstrando na prática os conceitos estudados na disciplina.

O projeto utiliza uma **lista simplesmente encadeada** como estrutura principal de armazenamento, além de implementar seis algoritmos de ordenação e busca sequencial.

A aplicação dispõe de uma interface web desenvolvida em HTML, CSS e JavaScript, integrada ao backend Python por meio do Flask.

**Importante:** o Citizen Tech é um protótipo educacional. Não representa um órgão governamental, não realiza consultas cadastrais oficiais, não emite documentos e não efetua agendamentos.

### Desafio oficial

https://experience.fiap.com.br/global-solution-citizen-tech

---

## 2. Objetivos

### Objetivo geral

Desenvolver um sistema de gerenciamento de informações sobre serviços públicos, aplicando estruturas de dados, algoritmos de busca, métodos de ordenação e conceitos de análise de complexidade computacional.

### Objetivos específicos

- Implementar uma lista simplesmente encadeada.
- Representar serviços públicos por meio de classes Python.
- Permitir o cadastro de múltiplos registros.
- Gerar identificadores aleatórios e únicos.
- Implementar operações de inserção, consulta, atualização e exclusão.
- Desenvolver mecanismos de busca sequencial.
- Implementar diferentes algoritmos de ordenação.
- Demonstrar visualmente as etapas de execução dos algoritmos.
- Contabilizar comparações, trocas, movimentações e inserções.
- Realizar testes automatizados das estruturas e algoritmos.
- Disponibilizar uma interface web para interação com o sistema.

---

## 3. Tecnologias utilizadas

| Tecnologia | Aplicação |
|---|---|
| Python | Linguagem principal e implementação dos algoritmos |
| Flask | Comunicação entre frontend e backend |
| HTML5 | Estrutura da interface |
| CSS3 | Estilização e responsividade |
| JavaScript | Interatividade e comunicação HTTP |
| JSON | Formato de troca de dados entre frontend e backend |
| Git | Controle de versão |
| GitHub | Armazenamento do código-fonte |

### Bibliotecas Python

| Biblioteca | Utilização |
|---|---|
| Flask | Aplicação web |
| Dataclasses | Modelagem dos registros |
| Random | Geração de identificadores |
| Pathlib | Manipulação de caminhos |
| Collections/estruturas nativas | Recursos auxiliares quando aplicáveis |

A implementação dos métodos de ordenação não depende das funções prontas de ordenação do Python.

---

## 4. Arquitetura do sistema

O Citizen Tech utiliza uma arquitetura dividida em frontend e backend.

### Frontend

Responsável pela interação com o usuário.

Permite preencher formulários, selecionar operações, executar algoritmos e visualizar os resultados.

### Backend

Responsável pelo processamento das operações, gerenciamento dos registros e execução das estruturas de dados e algoritmos.

### Fluxo de funcionamento

```text
                  USUÁRIO
                     |
                     v
              INTERFACE WEB
              HTML / CSS / JS
                     |
                     v
               REQUISIÇÃO HTTP
                     |
                     v
                 FLASK
                 main.py
                     |
                     v
              GERENCIAMENTO
             gerenciamento.py
                     |
          +----------+----------+
          |                     |
          v                     v
    LISTA ENCADEADA        ALGORITMOS
       lista.py          busca / ordenação
          |                     |
          v                     v
    NÓS E SERVIÇOS       RESULTADOS E MÉTRICAS
          |                     |
          +----------+----------+
                     |
                     v
                RESPOSTA JSON
                     |
                     v
                INTERFACE WEB
```

A lógica de gerenciamento e os algoritmos são processados no backend Python.

O JavaScript envia solicitações ao servidor e apresenta os resultados retornados.

---

## 5. Modelo dos registros

Cada serviço público é representado por um objeto da classe `Servico`.

Os registros possuem os seguintes atributos:

| Atributo | Descrição |
|---|---|
| `id` | Identificador único do serviço |
| `titulo` | Nome do serviço |
| `categoria` | Categoria do atendimento |
| `descricao` | Descrição do serviço |
| `requisitos` | Informações necessárias para atendimento |
| `local` | Local de atendimento informado |

### Categorias disponíveis

- RG
- CPF
- CNH
- Assistência Social

### Exemplo de registro fictício

```python
Servico(
    id=4821,
    titulo="Segunda via do RG",
    categoria="RG",
    descricao="Exemplo de serviço de identificação",
    requisitos="Consultar os requisitos oficiais",
    local="Local de atendimento"
)
```

O exemplo é ilustrativo e não representa orientação oficial sobre procedimentos ou documentos.

### Identificadores

Os IDs são gerados aleatoriamente no intervalo de 1000 a 9999.

Antes de cadastrar um novo serviço, o sistema verifica se o identificador já existe na lista encadeada.

Caso exista, outro número é gerado.

Isso evita duplicidade de IDs entre os registros ativos.

---

## 6. Lista simplesmente encadeada

A principal estrutura de dados do Citizen Tech é uma **lista simplesmente encadeada**, implementada com classes, objetos e referências em Python.

Cada nó possui:

- Um objeto `Servico`.
- Uma referência para o próximo nó.

### Representação

```text
  INÍCIO
     |
     v
+----------+     +----------+     +----------+
| ID: 4821 | --> | ID: 1934 | --> | ID: 7652 |
| RG       |     | CPF      |     | CNH      |
+----------+     +----------+     +----------+
                                        |
                                        v
                                       None
```

Os registros são conectados conforme a ordem de inserção.

A ordem dos IDs não precisa ser crescente, pois os identificadores são gerados aleatoriamente.

### Operações implementadas

**Inserção:** cria um novo nó e o adiciona ao final da lista.

**Percurso:** percorre os nós a partir do início para recuperar os registros.

**Remoção:** identifica o nó desejado e reorganiza as referências para preservar a integridade da estrutura.

A implementação também mantém referências para o primeiro e o último nó.

### Complexidade das operações

| Operação | Complexidade |
|---|---|
| Inserção ao final com referência ao último nó | O(1) |
| Percurso completo | O(n) |
| Busca sequencial | O(n) no pior caso |
| Remoção por ID | O(n) no pior caso |
| Consulta por ID | O(n) no pior caso |

A inserção física do nó ao final é O(1). Entretanto, o cadastro completo também realiza uma verificação de unicidade do ID, que pode exigir um percurso pela lista.

---

## 7. Operações de gerenciamento — CRUD

O sistema implementa as quatro operações fundamentais de gerenciamento de registros.

### Create — Cadastrar

Permite cadastrar serviços informando título, categoria, descrição, requisitos e local.

O identificador é gerado automaticamente.

### Read — Consultar

Permite consultar um registro por ID, listar os serviços cadastrados e pesquisar informações por título ou categoria.

### Update — Atualizar

Permite modificar as informações de um serviço já existente, utilizando seu identificador.

### Delete — Excluir

Permite remover um registro da lista encadeada.

A exclusão reorganiza as referências dos nós para manter o funcionamento da estrutura.

### Funcionalidades adicionais

- Gerar cinco registros fictícios.
- Limpar os registros cadastrados.
- Contabilizar serviços por categoria.
- Apresentar a quantidade total de serviços.
- Executar algoritmos de ordenação por ID.

---

## 8. Algoritmos de busca

O sistema utiliza **busca sequencial** para localizar os registros da lista encadeada.

### Busca por ID

Percorre os nós até encontrar o identificador informado.

Se o registro não existir, a busca retorna `None`, que é tratado pela camada de gerenciamento.

### Busca por título

Percorre os registros e verifica se o texto pesquisado está contido no título do serviço.

### Busca por categoria

Percorre os registros e retorna aqueles que correspondem ao texto informado na pesquisa.

As buscas textuais utilizam `casefold()`, permitindo comparações sem diferenciação entre letras maiúsculas e minúsculas.

### Complexidade

| Situação | Complexidade |
|---|---|
| Registro encontrado no primeiro nó | O(1) |
| Registro encontrado no último nó | O(n) |
| Registro inexistente | O(n) |
| Busca textual por todos os registros | O(n), considerando comparações de texto de tamanho limitado |

Na busca sequencial, o custo depende da quantidade de registros percorridos.

---

## 9. Algoritmos de ordenação

O Citizen Tech implementa seis algoritmos de ordenação por identificador.

Cada algoritmo utiliza uma cópia da sequência de registros, preservando a ordem original da lista encadeada.

### 9.1. Bubble Sort

Compara elementos adjacentes e realiza trocas quando estão fora da ordem desejada.

O processo é repetido até que não sejam necessárias novas trocas.

**Métricas registradas:**
- Comparações.
- Trocas.
- Etapas da execução.

### 9.2. Selection Sort

Percorre a parte ainda não ordenada para localizar o menor elemento.

Após identificá-lo, coloca-o na posição correspondente.

**Métricas registradas:**
- Comparações.
- Trocas.
- Etapas da execução.

### 9.3. Insertion Sort

Percorre a sequência e insere cada elemento na posição adequada entre aqueles já processados.

**Métricas registradas:**
- Comparações.
- Movimentações.
- Etapas da execução.

### 9.4. Merge Sort

Utiliza a estratégia de **divisão e conquista**.

A sequência é dividida recursivamente em partes menores, que depois são intercaladas de maneira ordenada.

**Métricas registradas:**
- Comparações.
- Movimentações.
- Divisões e intercalações.

### 9.5. Quick Sort

Utiliza um pivô para particionar a sequência.

Na implementação utilizada, o último elemento da partição é escolhido como pivô.

As partições são processadas recursivamente até a conclusão da ordenação.

**Métricas registradas:**
- Comparações.
- Trocas.
- Etapas do particionamento.

### 9.6. Tree Sort

Utiliza uma **árvore binária de busca**.

Os registros são inseridos na árvore conforme seus identificadores.

Posteriormente, é realizado um percurso em ordem para obter a sequência ordenada.

**Métricas registradas:**
- Comparações.
- Inserções na árvore.
- Movimentações.
- Etapas da execução.

A árvore utilizada não possui balanceamento automático.

---

## 10. Análise de complexidade — Big-O

A notação Big-O permite analisar como o custo de um algoritmo cresce conforme a quantidade de registros.

### Comparação dos algoritmos

| Algoritmo | Melhor caso | Caso médio | Pior caso |
|---|---|---|---|
| Bubble Sort otimizado | O(n) | O(n²) | O(n²) |
| Selection Sort | O(n²) | O(n²) | O(n²) |
| Insertion Sort | O(n) | O(n²) | O(n²) |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) |
| Quick Sort | O(n log n) | O(n log n) | O(n²) |
| Tree Sort | O(n log n) | O(n log n) | O(n²) |

### Considerações

O **Bubble Sort** apresenta comportamento quadrático na maioria dos casos, mas a versão implementada interrompe antecipadamente a execução quando a sequência já está ordenada.

O **Selection Sort** realiza um número quadrático de comparações, independentemente da ordem inicial dos dados.

O **Insertion Sort** apresenta bom desempenho quando os elementos já estão ordenados ou próximos da ordem correta.

O **Merge Sort** mantém complexidade O(n log n) nos casos analisados pela teoria do algoritmo.

O **Quick Sort** geralmente apresenta desempenho O(n log n), mas pode atingir O(n²) quando o particionamento é muito desequilibrado.

O **Tree Sort** depende do formato da árvore. Uma árvore desbalanceada pode produzir comportamento quadrático.

### Observação sobre a demonstração

Os valores da tabela descrevem a complexidade dos algoritmos de ordenação.

O registro detalhado de cada etapa para visualização acrescenta custos de memória e processamento que dependem da quantidade de passos armazenados.

---

## 11. Interface web

A interface foi desenvolvida em HTML, CSS e JavaScript.

Os botões da aplicação executam operações disponibilizadas pelo backend Flask.

### Gerenciamento

| Botão | Funcionalidade |
|---|---|
| Cadastrar serviço | Insere um registro |
| Consultar ID | Localiza um serviço |
| Listar serviços | Percorre e apresenta a lista |
| Buscar título | Pesquisa pelo título |
| Buscar categoria | Pesquisa pela categoria |
| Atualizar serviço | Modifica um registro |
| Excluir serviço | Remove um registro |
| Gerar 5 fictícios | Cria registros para testes |
| Analisar registros | Conta serviços e categorias |
| Limpar lista | Remove todos os registros da sessão |

### Ordenação

A interface também disponibiliza botões para:

- Bubble Sort.
- Selection Sort.
- Insertion Sort.
- Merge Sort.
- Quick Sort.
- Tree Sort.

Após selecionar um algoritmo, o usuário pode acompanhar os passos da execução por meio dos botões **Anterior** e **Próximo passo**.

A visualização apresenta a sequência de IDs e as métricas registradas pelo backend.

---

## 12. Testes automatizados

O arquivo `backend/teste.py` contém verificações dos algoritmos de ordenação e de operações da lista encadeada.

### Cenários de ordenação

Os seis algoritmos são aplicados a oito sequências:

1. Sequência desordenada.
2. Lista vazia.
3. Lista com um elemento.
4. Lista ordenada.
5. Lista em ordem inversa.
6. Sequência de nove elementos desordenados.
7. Sequência com valores de centenas.
8. Sequência contendo IDs repetidos.

Isso totaliza **48 verificações de ordenação configuradas**.

O resultado de cada algoritmo é comparado com uma sequência de referência gerada por `sorted()`.

A função pronta é utilizada exclusivamente para verificar os resultados nos testes, não para executar a ordenação principal da aplicação.

### Testes da lista encadeada

O arquivo também verifica:

- Inserção de registros.
- Busca por ID existente.
- Busca por ID inexistente.
- Remoção de registros.
- Remoção de elementos até esvaziar a lista.
- Tentativa de remoção de ID inexistente.
- Integridade das referências `inicio` e `ultimo`.

Os resultados devem ser confirmados pela execução do arquivo no ambiente Python.

---

## 13. Como executar o projeto

### Pré-requisitos

- Python instalado.
- Git instalado, caso o repositório seja clonado.
- Navegador web.
- Bibliotecas do arquivo `requirements.txt`.

Não é necessário utilizar banco de dados, chave de API ou serviços governamentais externos.

### 13.1. Clonar o repositório

```bash
git clone https://github.com/natan-costa01/GS_DSA.git
cd GS_DSA
```

### 13.2. Criar ambiente virtual

```powershell
python -m venv .venv
```

### 13.3. Ativar o ambiente virtual

No PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 13.4. Instalar as dependências

```powershell
python -m pip install -r requirements.txt
```

### 13.5. Executar os testes

```powershell
python backend/teste.py
```

O terminal apresentará as sequências originais e ordenadas, além das métricas de cada algoritmo.

### 13.6. Executar o sistema

```powershell
python backend/main.py
```

### 13.7. Acessar a interface

Abra o navegador:

http://127.0.0.1:5000

O servidor Flask disponibiliza o frontend e recebe as solicitações dos botões.

Para encerrar o servidor, pressione `Ctrl + C` no terminal.

---

## 14. Estrutura do projeto

```text
GS_DSA/
|
|-- backend/
|   |
|   |-- algoritmos/
|   |   |-- busca.py
|   |   |-- ordenacao.py
|   |
|   |-- models/
|   |   |-- no.py
|   |   |-- servico.py
|   |
|   |-- services/
|   |   |-- gerenciamento.py
|   |
|   |-- structures/
|   |   |-- arvore.py
|   |   |-- lista.py
|   |
|   |-- main.py
|   |-- teste.py
|
|-- frontend/
|   |-- index.html
|   |-- script.js
|   |-- style.css
|
|-- requirements.txt
```

### Organização dos arquivos

| Arquivo | Responsabilidade |
|---|---|
| `servico.py` | Modelo dos serviços |
| `no.py` | Estrutura de um nó |
| `lista.py` | Lista encadeada |
| `arvore.py` | Nó da árvore binária |
| `busca.py` | Busca sequencial |
| `ordenacao.py` | Seis algoritmos de ordenação |
| `gerenciamento.py` | Operações CRUD e processamento |
| `main.py` | Servidor Flask |
| `teste.py` | Testes automatizados |
| `index.html` | Interface web |
| `style.css` | Estilização |
| `script.js` | Requisições e demonstrações |

---

## 15. Relação com os Objetivos de Desenvolvimento Sustentável

O Citizen Tech apresenta relação temática com os Objetivos de Desenvolvimento Sustentável (ODS).

### ODS 10 — Redução das Desigualdades

A proposta busca facilitar a organização e a consulta de informações sobre serviços públicos, contribuindo conceitualmente para a redução de barreiras informacionais.

### ODS 11 — Cidades e Comunidades Sustentáveis

A aplicação explora o uso de ferramentas digitais para organizar informações relacionadas aos serviços disponíveis ao cidadão.

Essas relações representam os objetivos da proposta acadêmica, não resultados de impacto social medidos.

---

## 16. Limitações do projeto

O Citizen Tech é um protótipo acadêmico desenvolvido para demonstrar estruturas de dados e algoritmos.

Suas principais limitações são:

- Armazenamento dos registros apenas em memória.
- Perda dos registros quando o servidor é encerrado.
- Ausência de banco de dados persistente.
- Ausência de integração com sistemas governamentais.
- Geração de registros fictícios para os testes.
- Ausência de autenticação e controle de acesso.
- Ausência de emissão de documentos ou agendamentos.
- Limitações de desempenho da árvore binária não balanceada.
- Registro de passos voltado à demonstração acadêmica.

As informações inseridas no sistema não substituem orientações disponibilizadas por órgãos públicos oficiais.

---


## 17. Considerações finais

O Citizen Tech demonstra a aplicação prática de estruturas de dados e algoritmos em um sistema de gerenciamento de informações sobre serviços públicos.

A implementação de uma lista simplesmente encadeada permite compreender o funcionamento das operações de inserção, percurso, busca e remoção por meio de referências entre nós.

Os seis algoritmos de ordenação possibilitam observar diferentes estratégias de organização dos registros, incluindo comparação de elementos, deslocamentos, divisão e conquista, particionamento e árvores binárias de busca.

A interface web permite acompanhar o comportamento dos algoritmos de maneira interativa, enquanto os testes automatizados oferecem mecanismos para verificar a correção das sequências produzidas.

O projeto reúne conceitos fundamentais da disciplina de Data Structures and Algorithms, relacionando estruturas de dados, desenvolvimento de software e análise de complexidade computacional.

---

<div align="center">

**CITIZEN TECH**

Global Solution 2026.2

Data Structures and Algorithms

**FIAP**

https://github.com/natan-costa01/GS_DSA

</div>
