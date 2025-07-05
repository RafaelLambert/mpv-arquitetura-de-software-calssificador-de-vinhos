# MVP Classificador de Vinhos - Front-End

Este repositório contém a interface web do projeto MVP de classificação de vinhos, desenvolvido como parte da formação em Engenharia de Software na PUC-Rio. O front-end foi criado com HTML, CSS e JavaScript puro, e tem como objetivo permitir que o usuário interaja com a API REST de forma intuitiva e eficiente.

---

## 🧩 Funcionalidades

A interface permite:

- **Cadastro de Vinhos**  
  Um formulário completo para inserir os dados físico-químicos de um vinho. Após o envio, a API retorna automaticamente a classificação da qualidade do vinho (_Ruim_, _Razoável_, _Bom_ ou _Excelente_).

- **Listagem de Vinhos Cadastrados**  
  Exibe uma tabela com todos os vinhos registrados, incluindo:
  - Nome
  - Tipo (tinto ou branco)
  - Parâmetros físico-químicos
  - Qualidade
  - Ação para remoção

- **Busca por Nome**  
  Permite buscar vinhos pelo nome exato por meio de uma requisição GET.

- **Remoção de Vinhos**  
  Cada vinho exibido na tabela possui um botão de exclusão que remove o registro do banco de dados e da interface.

---

## 🚀 Como Executar o Front-End

### Pré-requisitos

- Ter o **back-end** da aplicação em execução localmente em `http://127.0.0.1:5000`.

### Passos

1. Clone este repositório ou copie os arquivos `index.html` e `script.js` para um diretório local.
2. Dê um duplo clique no arquivo `index.html` ou execute-o em um navegador de sua preferência.
3. Use a interface para:
   - Cadastrar novos vinhos
   - Listar os vinhos existentes
   - Buscar vinhos pelo nome
   - Remover registros da base

---

## 🌐 Integração com a API

A interface se comunica com os seguintes endpoints da API Flask:

- `POST /wine` — Cadastro de vinho + classificação
- `GET /wines` — Listagem de todos os vinhos
- `GET /wine?name={nome}` — Busca por nome
- `DELETE /wine?name={nome}` — Exclusão de vinho

---

## 📝 Observações

- Certifique-se de que o back-end esteja ativo antes de interagir com a interface.
- A comunicação é feita via `fetch()` utilizando `application/json`.

---

## 📄 Licença

Este front-end faz parte do MVP educacional desenvolvido para a disciplina de Engenharia de Software da PUC-Rio. Uso acadêmico e demonstrativo.
