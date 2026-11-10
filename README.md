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

| Integrante               | Responsabilidade                                                                   |
|--------------------------|------------------------------------------------------------------------            |
| **Maria Eduara Padilha** | Liderança do projeto, CSS de produtos, README e desenvolvimento do app `produtos`  |
| **Felipe**               | Integração do Django, Home, Dashboard, URLs principais e integração dos templates             |
| **Maria Clara**          | Desenvolvimento da página de categoria e contato                                               |
| **Mayara**               | Desenvolvimento da página de login e cadastro                             |

### Maria Eduarda Padilha — Produto + Liderança

Responsável pela liderança do projeto e pelo sistema de produtos.

* Liderança do projeto;
* Desenvolvimento do CSS;
* Criação, Atualização e manutenção do README;
* Desenvolvimento do app `produtos`;
* Model `Produto`;
* Forms de produtos;
* Views de produtos;
* URLs do produto;
* Admin do produto.

### Felipe — Integração Django + Home + Dashboard

Responsável pela integração do projeto com o Django, pelo funcionamento da página inicial e pelo desenvolvimento do painel administrativo.

* `config/urls.py`;
* View da Home;
* Integração das URLs;
* Ligação dos templates com o Django;
* Página `index`;
* Integração da Home com os produtos cadastrados;
* Testes das rotas e funcionalidades.
* view do dashboard.
* template do dashboard.
* Configuração da URL do Dashboard.
  

### Maria Clara — Contato e Categoria

Responsável pelo desenvolvimento da página de contato e categoria da loja.

* Página de contato e categorias;
* View de contato e categoria;
* URL de contato e categoria;
* models de contato e categoria
* apps de contato e categoria
* Template de contato e categorias;
* css de contato e categorias
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
* criação do app 'usuarios'
* criação da tela de login

---

## Apps Django

### `produtos`

**Responsável:** Maria Eduarda Padilha

**Finalidade:**
O app `produtos` será responsável pelo gerenciamento dos produtos da loja MafeBeauty.

O app concentrará as funcionalidades relacionadas ao cadastro, visualização, edição e exclusão dos produtos.

### `usuarios`
**Responsável:** Mayara Borges

**Finalidade:**
O app `usuarios` será responsável pela definição de acesso de caa um, apartir da tela de login.

O app concentrará as funcionalidades relacionadas ao login, contato e acesso restrito para cada usuario.

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

### Dashboard

**Responsável:** Felipe

O Dashboard será responsável pelo painel administrativo do sistema, centralizando o acesso às funcionalidades de gerenciamento da loja.

Sua finalidade é facilitar a administração e a organização das informações do sistema.

### Contato

**Responsável:** Maria Clara

A página de contato será responsável por apresentar as informações da loja e disponibilizar uma página específica para contato.

Caso necessário, será desenvolvida uma View e uma URL específica para a página.

### app usuarios e tela de login

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

### Felipe — Integração Django + Home + Dashboard

| Arquivo/Área | Responsabilidade |
|---|---|
| `config/urls.py` | Integração das URLs do projeto |
| View da Home | Desenvolvimento da View da página inicial |
| `index.html` | Integração da página inicial com o Django |
| Templates | Ligação dos templates com o Django |
| Integração com produtos | Exibição dos produtos cadastrados na Home |
| View do Dashboard | Desenvolvimento da View do painel administrativo |
| Template do Dashboard | Desenvolvimento da interface do painel |
| URL do Dashboard | Configuração da rota do painel administrativo |
| Rotas | Testar e corrigir as rotas do projeto |

### Maria Clara — Contato

| Arquivo/Área        | Responsabilidade                                                      |
| ------------------- | ----------------------------------------------------------------------|
| `contato.html`      | Desenvolvimento da página de contato                                  |
| View de contato     | Criar a View caso seja necessária                                     |
| URL de contato      | Configuração da rota da página de contato                             |
| models de contato   | Criação do model para armazenar as mensagens enviadas pelo formulário |
| apps de contato     | Criação e configuração do aplicativo de contato                       |                                                                       |
| `contato.css`       | Ajustes visuais da página                                             |
| Informações da loja | Inserção e organização das informações de contato                     |
| Testes              | Testar o funcionamento da página                                      |

### Maria Clara — Categoria

| Arquivo/Área          | Responsabilidade                                                  |
| -------------------   | ------------------------------------------------------------------|
| `categoria.html`      | Desenvolvimento da página de categoria                            |
| View de categoria     | Criar a View caso seja necessária                                 |
| URL de categoria      | Configuração da rota da página de categoria                       |
| models de categoria   |  Criação do model para armazenar as categorias no banco de dados  |
| apps de categoria     |  Criação e configuração do aplicativo de categorias               |
| `categoria.css`       | Ajustes visuais da página                                         |
| Informações da loja   | Inserção e organização das informações de categoria               |
| Testes                | Testar o funcionamento da página                                  |


### Mayara — Templates e Acabamento e criação do app usuarios

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

A **Maria Eduarda Padilha** ficará responsável pelo sistema de produtos e pela liderança do projeto. O **Felipe** ficará responsável pela integração do Django pela Home,pelo Dashboard e pelas URLs principais. A **Maria Clara** ficará responsável pela página de contato. A **Mayara** ficará responsável pela revisão dos templates, navegação restrita de cada usuario atravez da tela de login e criação de 'usuarios'.

Dessa forma, as partes desenvolvidas individualmente poderão ser integradas em um único sistema web funcional.

---

## Repositório

**Projeto:** MafeBeauty

**GitHub:** `mafebeautyatu`
