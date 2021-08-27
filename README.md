# IFPizzaPython
<p>Pagina Web Utilizando Python e Django. Sistema criado como atividade para conceito da matéria de Desenvolvimento Web (Professor Frank) e Construção de Software (Professor Marcelo). 
<p>Neste projeto é realizado uma simples página para delivery de Pizza, onde é feito todo o CRUD de Produto (pizza) e Pedido (pedido do cliente). Utiliza-se dois tipos de usuários, primeiro temos o grupo de administrador que tem acesso 100% ao sistema e realiza todas as funções disponibilizadas, e por fim, temos o Cliente que pode realizar o pedido da pizza, selecionar endereço de entrega e editar estes se necessário.


# Perfis do Sistema
<p>Para que um usuário seja Administrado, acesse http://localhost:8000/admin/ e acesso o Login com o super usuário
admin / admin. Vá em "Usuários", escolha o que desejar e rolando um pouco a tela, ache a opção de "Permissões", clique em "Administrado" e na seta ao lado. No Final da página, clique em "Salva".

- Administrado/SuperUsuário
    <p> Login: admin
    <p> Senha: admin

- Cliente 
    -<p> Crie um Login com Nome e Senha desejada
    -<p> http://localhost:8000/registrar/


# Instalação do Projeto IF Pizza
Django utilaza-se a criação de ambientes virtuais de desenvolvimento, neste meu programa foi criado o ambiente virtual chamado "projeto". Estes ambientes são utilizados para que possa ser separado diferentes projeto, possibilitando assim que cada um utilize um versão do django, versões de bibliotecas etc...
Para que seja possível executar o programa deve ser feito os seguintes comandos na pasta que desejar, utilizando o exclusivamente o CMD.
- pip install --upgrade virtualenv
- pip install --upgrade virtualenvwrapper-win

Caso terminal peça a atualização do PIP, execute 
- pip install --upgrade pip

Para criar o ambiente virtual (recomenda-se criar do mesmo nome que o meu) "projeto"
- mkvirtualenv projeto 

Assim que criar o ambiente virtual o cmd estará dentro do projeto, conforme a imagem abaixo. 
<p aling="center">
    <img width="800" src="static\img\cmd.png">
</ p>

Agora execute
- pip install django==2.2.12
- pip install django-crispy-forms
- pip install django-braces
- pip install django-cleanup

OBS - Versão do Python utilizado 3.7.2


# Comandos de Inicialização do Projeto IF Pizza (cmd)
- workon projeto
    <p> Iniciar o ambiente virtual do Projeto 

- python manage.py runserver
    <p> Realizar o Start do Sistema

- OBS: Estes comandos devem ser executados na pasta raiz do projeto. Por exemplo, C:\Users\usuario\Documents\Programas\Pizza>
    
- pip install django-brace 
    <p> Biblioteca que possibilita o gerênciamento de acesso de perfis

# Explicação de Pastas
- cadastro <p> Realizados todas as inserções das entidades
- paginas <p> Templates iniciais, da tela home, pedido
- usuários <p> Se tem os templates e links para perfis de usuários

# Rotas
- Home 
    -<p>http://localhost:8000/ (Página Inicial)

- Login
    -<p>http://localhost:8000/login/ (Realizar Login)
    -<p>http://localhost:8000/logout/ (Realizar Logout)

- Cadastrar
    -<p>http://localhost:8000/cadastrar/pedido/ (Cadastrar/Finalizar Pedido)
    -<p>http://localhost:8000/cadastrar/produto/ (Cadastrar Produto/Pizza)
    -<p>http://localhost:8000/adicionar/pizza/  (Realizar Pedido de Pizza)
    -<p> http://localhost:8000/registrar/ (Cadastrar um Login)

- Listar
    -<p>http://localhost:8000/listar/pedido/ (Listar Pedidos)
    -<p>http://localhost:8000/listar/produto/ (Listar Produtos)

- Atualizar
    -<p>http://localhost:8000/atualizar/pedido/id{} (Atualizar Pedido específico com ID)
    -<p>http://localhost:8000/atualizar/produto/id{} (Atualizar Produto específico com ID)

- Excluír
    -<p>http://localhost:8000/excluir/produto/id{} (Excluir Produto específico com ID)
 




