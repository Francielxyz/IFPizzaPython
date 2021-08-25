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


# Comandos que devem ser executados no Terminal da IDE (cmd)
- workon projeto
    <p> Iniciar o Projeto 

- python manage.py runserver
    <p> Realizar o Start do Programa
    
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
 




