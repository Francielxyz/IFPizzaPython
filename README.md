# IFPizzaPython
<p>Pagina Web Utilizando Python e Django. Sistema criado como atividade para conceito da matéria de Desenvolvimento Web (Professor Frank) e Construção de Software (Professor Marcelo). 
<p>Neste projeto é realizado uma simples página para delivery de Pizza, onde é feito todo o CRUD de Produto (pizza) e Pedido (pedido do cliente). Utiliza-se dois tipos de usuários, primeiro temos o grupo de adminitrador que tem acesso 100% ao sistema e realiza todas as funções disponibilizads, e por fim, temos o Cliente que pode realizar o pedido da pizza, selecionar endereço de entrega e editar estes se necessário.

# Perfis do Sistema
- Administrado 
    <p> Login: admin
    <p> Senha: admin
- Cliente 
    <p> Login: Franciel_Ruam
    <p> Senha: fr89fr89

# Comandos que devem ser executados
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
    -<p>http://localhost:8000/

- Login
    -<p>http://localhost:8000/login/
    -<p>http://localhost:8000/logout/

- Cadastrar
    -<p>http://localhost:8000/cadastrar/pedido/
    -<p>http://localhost:8000/cadastrar/produto/
    -<p>http://localhost:8000/adicionar/pizza/

- Listar
    -<p>http://localhost:8000/listar/pedido/
    -<p>http://localhost:8000/listar/produto/
    -<p>http://localhost:8000/pedido/

- Atualizar
    -<p>http://localhost:8000/atualizar/pedido/id{}
    -<p>http://localhost:8000/atualizar/produto/id{}

- Excluír
    -<p>http://localhost:8000/excluir/pedido/id{}
    -<p>http://localhost:8000/excluir/produto/id{}





