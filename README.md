# MafeBeauty

## Nome do Projeto

**MafeBeauty**

---

## Descrição do Projeto

O **MafeBeauty** é um sistema web desenvolvido para uma loja de produtos de maquiagem e beleza.

O projeto tem como objetivo apresentar os produtos disponíveis na loja, organizar suas informações e facilitar a navegação dos usuários pelo site.

O sistema será desenvolvido utilizando Django, permitindo a integração entre as páginas do site, o banco de dados e as funcionalidades de gerenciamento dos produtos.

---

## Tecnologias Utilizadas

As principais tecnologias utilizadas no desenvolvimento do projeto são:

* **Python**
* **Django**
* **HTML**
* **CSS**
* **JavaScript**
* **Bootstrap**
* **SQLite**
* **Git**
* **GitHub**

---

## Equipe

| Integrante               | Responsabilidade                                                       |
|--------------------------| ---------------------------------------------------------------------- |
| **Maria Eduara Padilha** | Liderança do projeto, CSS, README e desenvolvimento do app `produtos`  |
| **Felipe**               | Integração do Django, Home, URLs principais e integração dos templates |
| **Maria Clara**          | Desenvolvimento da página de contato                                   |
| **Mayara**               | Revisão dos templates, navegação, responsividade e acabamento visual   |

### Maria Eduarda Padilha — Produto + Liderança

Responsável pela liderança do projeto e pelo sistema de produtos.

* Liderança do projeto;
* Desenvolvimento do CSS;
* Criação, Atualização e manutenção do README;
* Desenvolvimento do app `produtos`;
* Model `Produto`;
* Forms;
* Views;
* URLs do produto;
* Admin do produto.

### Felipe — Integração Django + Home

Responsável pela integração do projeto com o Django e pelo funcionamento da página inicial.

* `config/urls.py`;
* View da Home;
* Integração das URLs;
* Ligação dos templates com o Django;
* Página `index`;
* Integração da Home com os produtos cadastrados;
* Testes das rotas.

### Maria Clara — Contato

Responsável pelo desenvolvimento da página de contato da loja.

* Página de contato;
* View de contato, caso seja necessária;
* URL de contato;
* Template de contato;
* Informações da loja;
* Ajustes no `contato.css`;
* Testes da página.

### Mayara — Templates e Acabamento

Responsável pela revisão dos templates e pelo acabamento visual e de navegação do sistema.

* Revisar os templates;
* Verificar os links do menu;
* Verificar a navegação entre as páginas;
* Conferir a responsividade;
* Conferir o uso do Bootstrap;
* Corrigir pequenos problemas visuais;
* Testar as páginas no navegador.

---

## Apps Django

### `produtos`

**Responsável:** Maria Eduarda Padilha

**Finalidade:**
O app `produtos` será responsável pelo gerenciamento dos produtos da loja MafeBeauty.

O app concentrará as funcionalidades relacionadas ao cadastro, visualização, edição e exclusão dos produtos.

---

## Models e Views

### App `produtos`

#### Model — `Produto`

O Model `Produto` será responsável por armazenar as informações dos produtos da loja.

As informações do produto poderão incluir:

* Nome;
* Descrição;
* Imagem;
* Categoria;
* Outras informações necessárias ao sistema.

**Responsável:** Maria Eduarda Padilha

#### Views

As Views do app `produtos` serão responsáveis pelas principais funcionalidades do sistema de produtos:

* Listagem dos produtos;
* Visualização dos detalhes de um produto;
* Cadastro de produtos;
* Edição de produtos;
* Exclusão de produtos.

**Responsável:** Maria Eduarda Padilha

### Home

**Responsável:** Felipe

A Home será responsável pela página inicial do sistema e pela integração entre os templates, URLs e funcionalidades do Django.

Também será realizada a integração da Home com os produtos cadastrados no sistema.

### Contato

**Responsável:** Maria Clara

A página de contato será responsável por apresentar as informações da loja e disponibilizar uma página específica para contato.

Caso necessário, será desenvolvida uma View e uma URL específica para a página.

### Templates e acabamento

**Responsável:** Mayara

Será realizada a revisão dos templates existentes, verificando:

* Navegação;
* Links;
* Responsividade;
* Integração entre páginas;
* Uso do Bootstrap;
* Organização visual.

---

## Arquivos e Responsabilidades

### Maria Eduarda Padilha — Produtos + Liderança

| Arquivo/Área         | Responsabilidade                                 |
| -------------------- | ------------------------------------------------ |
| `produtos/models.py` | Desenvolvimento do Model `Produto`               |
| `produtos/forms.py`  | Desenvolvimento dos Forms                        |
| `produtos/views.py`  | Desenvolvimento das Views de produtos            |
| `produtos/urls.py`   | Criação das URLs do app                          |
| `produtos/admin.py`  | Configuração do produto no painel administrativo |
| `static/css/`        | Desenvolvimento e manutenção do CSS              |
| `README.md`          | Documentação e atualização do projeto            |

### Felipe — Integração Django + Home

| Arquivo/Área            | Responsabilidade                          |
| ----------------------- | ----------------------------------------- |
| `config/urls.py`        | Integração das URLs do projeto            |
| View da Home            | Desenvolvimento da View da página inicial |
| `index.html`            | Integração da página inicial com o Django |
| Templates               | Ligação dos templates com o Django        |
| Integração com produtos | Exibição dos produtos cadastrados na Home |
| Rotas                   | Testar e corrigir as rotas do projeto     |

### Maria Clara — Contato

| Arquivo/Área        | Responsabilidade                                  |
| ------------------- | ------------------------------------------------- |
| `contato.html`      | Desenvolvimento da página de contato              |
| View de contato     | Criar a View caso seja necessária                 |
| URL de contato      | Criar a rota da página                            |
| `contato.css`       | Ajustes visuais da página                         |
| Informações da loja | Inserção e organização das informações de contato |
| Testes              | Testar o funcionamento da página                  |

### Mayara — Templates e Acabamento

| Arquivo/Área   | Responsabilidade                                       |
| -------------- | ------------------------------------------------------ |
| Templates HTML | Revisão e organização                                  |
| Menu           | Conferência dos links                                  |
| Navegação      | Teste da navegação entre páginas                       |
| Responsividade | Conferência das páginas em diferentes tamanhos de tela |
| Bootstrap      | Conferência da utilização                              |
| CSS            | Correção de pequenos problemas visuais                 |
| Navegador      | Testes finais das páginas                              |

---

## Organização das Responsabilidades

A divisão das tarefas foi realizada para que cada integrante tenha uma área específica do projeto, facilitando o desenvolvimento e a integração das funcionalidades.

A **Maria Eduarda Padilha** ficará responsável pelo sistema de produtos e pela liderança do projeto. O **Felipe** ficará responsável pela integração do Django e pela Home. A **Maria Clara** ficará responsável pela página de contato. A **Mayara** ficará responsável pela revisão dos templates, navegação, responsividade e acabamento visual.

Dessa forma, as partes desenvolvidas individualmente poderão ser integradas em um único sistema web funcional.

---

## Repositório

**Projeto:** MafeBeauty

**GitHub:** `mafebeautyatu`
