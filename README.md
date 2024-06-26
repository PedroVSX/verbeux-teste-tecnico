# Arquivos
- [chatbot-avaliacoes-firebase-adminsdk-e8k2s-edbb8c5bea.json](https://github.com/PedroVSX/verbeux-teste-tecnico/blob/main/teste-tecnico/chatbot-avaliacoes-firebase-adminsdk-e8k2s-edbb8c5bea.json) Arquivo para conexão ao banco de dados Firebase.
- [main.py](https://github.com/PedroVSX/verbeux-teste-tecnico/blob/main/teste-tecnico/main.py) Arquivo main, todo o código para usar o chatbot está aqui.

**AVISO!!!**
- Coloque [chatbot-avaliacoes-firebase-adminsdk-e8k2s-edbb8c5bea.json](https://github.com/PedroVSX/verbeux-teste-tecnico/blob/main/teste-tecnico/chatbot-avaliacoes-firebase-adminsdk-e8k2s-edbb8c5bea.json) no mesmo endereço de [main.py](https://github.com/PedroVSX/verbeux-teste-tecnico/blob/main/teste-tecnico/main.py) e mude no código o endereço na variável *cred* para o endereço do seu computador!!!

# Esclarecimentos
- O chatbot usado foi o de abordagem por fluxo.
- O código foi escrito em inglês! Mas os textos para visualização do usuário estão em português.
- A visualização do projeto é pelo terminal.

# Descrição do projeto
O código foi escrito em Python, os imports usados são: *requests* e *firebase_admin*;

No código terá vários métodos:
- *get_new_chat()*
  - Na variável *data*, eu coloco as informações do meu chatbot.
  - Tenho que explicar um pouco sobre a minha variável response, eu não conseguia de jeito nenhum iniciar uma sessão com o chatbot, então busquei outra solução. Na minha tela de fluxo do chatbot, cliquei para conversar com o bot, cliquei para inspecionar a página, fui para a aba network e peguei o link [https://api.verbeux.com.br/dialog-manager-proxy/](https://api.verbeux.com.br/dialog-manager-proxy/), que é a request do chat. Daí, só coloquei os dados do chatbot e sua chave API.
  - Se tudo der certo, ele retorna os dados JSON da response.

- *send_message(chat_id, message)*
  - Na variável *data*, eu coloco a mensagem.
  - O meu response eu faço uma solicitação de PUT à API, onde coloco o *data* e a minha chave.
  - Se tudo der certo, ele me retorna a primeira reposta do chat.
  
- *add_database(message, positive)*
  - Ele pega a variável *message* e coloca dentro de *review*, que é basicamente um campo de um documento do banco de dados.
  - Na chamada do método, que está mais abaixo dele, o código realiza uma separação de avaliação (positiva ou negativa), e na chamada, se for positiva insere como parâmetro *True*, senão insere *False*.
  - Dentro do método, o código verifica se é positivo ou não, cria um no banco de dados documento e coloca *review* dentro de *PositiveReviews* ou *NegativeReviews*, que são coleções do banco de dados.

- *print_database()*
  - Basicamente, ele pega todos os documentos das coleções e printa o *id* e a *review* de cada um.

Há algumas variáveis definidas no ínicio, que são a *snapshot_version*, *api_key* e um *headers* que é um dicionário que recebe *api_key*.

No código há uma variável *cred* que basicamente é o endereço em que o [chatbot-avaliacoes-firebase-adminsdk-e8k2s-edbb8c5bea.json](https://github.com/PedroVSX/verbeux-teste-tecnico/blob/main/teste-tecnico/chatbot-avaliacoes-firebase-adminsdk-e8k2s-edbb8c5bea.json) se encontra, é necessário ele estar no mesmo endereço que [main.py](https://github.com/PedroVSX/verbeux-teste-tecnico/blob/main/teste-tecnico/main.py), portanto você terá que colocar no código o endereço que você salvou no seu computador para funcionar o programa.

Abaixo disso, há uma variável *db* que é a instanciação do meu banco de dados Firebase.

Mais abaixo há um menu, que foi feito utilizando *while*, que pega a escolha do usuário e realiza a ação que ele desejar.

No código para conversar com o chatbot (escolha 1), há o input de mensagens e o retorno do *response*, que será importante, pois este faz as verificações se a resposta do bot é uma despedida, se é uma avaliação positiva ou negativa.

No código para visualizar as avaliações (escolha 2), o programa coloca dentro de uma variável *collections* todas as coleções disponíveis no meu banco de dados (no caso NegativeReviews e PositiveReviews). Em seguida, um loop é realizado para printar o id da coleção e depois uma chamada de método print_database() printará todos os documentos que estão dentro de cada coleção.

Na escolha de sair (escolha 0), o programa para.

# Instruções para usar o projeto
- Execute o arquivo [main.py](https://github.com/PedroVSX/verbeux-teste-tecnico/blob/main/teste-tecnico/main.py);

- No terminal, aparecerá um menu com 3 opções:
  1. Falar com chatbot
  2. Ver avaliações
  3. Sair

- Caso execute i:
  - Primeiramente, cumprimente o chatbot, digite "Oi" ou "Olá".
  - Logo em seguida, o bot pedirá para você realizar a sua avaliação, portanto digite a sua avaliação sobre alguma loja. Ex: "Eu adorei a comida do McDonald's, ela é simplesmente sensacional!", "Gostaria de avaliar o Burger King, os hambúrgueres deles são terríveis".
  - Caso queira realizar mais alguma avaliação, digite novamente ela.
  - Para sair da conversa com o bot, se despeça dele, digite "Adeus" ou "Tchau".

- Caso execute ii:
  - Basicamente, o código irá printar automaticamente todas avaliações disponíveis no banco de dados.
 
- Caso execute iii:
  - O programa será encerrado.

# Finalização
Basicamente é isso!
