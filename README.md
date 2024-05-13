# Arquivos
- [chatbot-avaliacoes-firebase-adminsdk-e8k2s-edbb8c5bea.json](https://github.com/PedroVSX/verbeux-teste-tecnico/blob/main/teste-tecnico/chatbot-avaliacoes-firebase-adminsdk-e8k2s-edbb8c5bea.json) Arquivo para conexão ao banco de dados Firebase.
- [main.py](https://github.com/PedroVSX/verbeux-teste-tecnico/blob/main/teste-tecnico/main.py) Arquivo main, todo o código do chatbot está aqui.

# Esclarecimentos
O chatbot usado foi o de abordagem por fluxo.
O código foi escrito em inglês! Mas os textos para visualização do usuário estão em português.

# Descrição do projeto
O código foi escrito em Python;

Os imports usados são: requests e firebase_admin;

No código terá vários métodos:
- *get_new_chat()*
  - Na variável *data*, eu coloco as informações do meu chatbot.
  - Tenho que explicar um pouco sobre a minha variável response, eu não conseguia de jeito nenhum iniciar uma sessão com o chatbot, então busquei outra solução. Na minha tela de fluxo do chatbot, cliquei para conversar com o     bot, cliquei para inspecionar a página, fui para a aba network e peguei o link [https://api.verbeux.com.br/dialog-manager-proxy/](https://api.verbeux.com.br/dialog-manager-proxy/), que é a request do chat. Daí, só coloquei os dados do chatbot e sua chave API.
  - Se tudo der certo, ele retorna os dados JSON da response.

- *send_message(chat_id, message)*
  - Na variável *data*, eu coloco a mensagem.
  - O meu response eu faço uma solicitação de PUT à API, onde coloco o *data* e a minha chave.
  - Se tudo der certo, ele me retorna a primeira reposta do chat.
  
- *add_database()*
- *print_database()*

