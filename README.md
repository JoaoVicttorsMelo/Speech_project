<div align="center"> <h1>🗣️ Assistente por voz IA </h1> <img src="https://img.shields.io/badge/Python-3.8%2B-blue" alt="Python Version"> <img src="https://img.shields.io/badge/License-MIT-green" alt="License"> <img src="https://img.shields.io/badge/Status-In%20Development-yellow" alt="Status"> </div> <div> <h2>📝 Descrição</h2> <p><strong>O Assistente por voz IA</strong> é um aplicativo em Python que utiliza reconhecimento de voz para interagir com o usuário. O assistente permite que o usuário converse, obtenha informações sobre clima, notícias, conversões de moedas, entre outras funcionalidades. O projeto usa APIs como OpenAI, NewsAPI, CurrencyConverterAPI e bibliotecas como <code>pyttsx3</code> para síntese de voz e <code>speech_recognition</code> para reconhecimento de fala.</p> </div> <div> <h2>🚀 Funcionalidades</h2> <ul> <li>🎙️ <strong>Reconhecimento de Fala</strong>: Captura e reconhece comandos de voz do usuário utilizando o microfone.</li> <li>💬 <strong>Respostas Baseadas em IA</strong>: Integração com a API da OpenAI para responder perguntas gerais e manter diálogos.</li> <li>☁️ <strong>Informações de Clima</strong>: Busca dados de clima em tempo real através de APIs especializadas.</li> <li>📰 <strong>Notícias em Tempo Real</strong>: Fornece notícias atualizadas sobre diversos tópicos usando a NewsAPI.</li> <li>💱 <strong>Conversão de Moedas</strong>: Converte valores entre diferentes moedas utilizando a CurrencyConverterAPI.</li> <li>🔄 <strong>Loop de Conversação</strong>: O programa continua ouvindo comandos até que o usuário diga "sair" ou "encerrar".</li> </ul> </div> <div> <h2>🛠️ Tecnologias Utilizadas</h2> <ul> <li><strong>Linguagem</strong>: <img src="https://img.shields.io/badge/-Python-blue" alt="Python"> Python 3.8+</li> <li><strong>Bibliotecas</strong>: <ul> <li><code>speech_recognition</code>: Para capturar e reconhecer a fala do usuário.</li> <li><code>pyttsx3</code>: Para síntese de fala (text-to-speech).</li> <li><code>requests</code>: Para realizar chamadas às APIs externas.</li> <li><code>openai</code>: Para integração com a API da OpenAI, gerando respostas baseadas em IA.</li> <li><code>pyyaml</code>: Para carregar configurações do arquivo YAML.</li> </ul> </li> </ul> </div> <div> <h2>📋 Pré-requisitos</h2> <ul> <li>Python 3.8 ou superior instalado.</li> <li>Microfone funcionando para captura de áudio.</li> <li>Conexão com a internet para realizar buscas e consultas em tempo real.</li> <li>Chaves de API para OpenAI, NewsAPI e CurrencyConverterAPI.</li> <li>Instalação das dependências listadas no <code>requirements.txt</code>.</li> </ul> </div> <div> <h2>🔧 Instalação</h2> <ol> <li> <p><strong>Clone o repositório</strong>:</p> <pre><code>git clone https://github.com/usuario/virtual-assistant-project.git cd virtual-assistant-project</code></pre> </li> <li> <p><strong>Instale as dependências</strong>:</p> <pre><code>pip install -r requirements.txt</code></pre> </li> </ol> </div> <div> <h2>🚀 Uso</h2> <ol> <li> <p><strong>Executando o Assistente Virtual</strong>:</p> <p>Você pode executar o script principal para iniciar o assistente virtual:</p> <pre><code>python main.py</code></pre> </li> <li> <p><strong>Interagindo com o Sistema</strong>:</p> <p>Fale comandos como "Qual o clima em Tóquio?", "Me diga as últimas notícias de tecnologia" ou "Converter 100 USD para BRL" e o sistema responderá de acordo com a API integrada.</p> </li> </ol> </div> <div> <h2>🗂️ Estrutura do Projeto</h2> <pre><code>VirtualAssistant/ ├── assistente.py ├── main.py ├── config.yml ├── .gitignore └── README.md</code></pre> <ul> <li><code>assistente.py</code>: Contém as funções que interagem com as APIs e processam as respostas.</li> <li><code>main.py</code>: Script principal que captura a fala e gerencia o fluxo de conversação.</li> <li><code>config.yml</code>: Arquivo de configuração que contém as chaves de API e outros parâmetros.</li> <li><code>.gitignore</code>: Arquivo que lista os arquivos e diretórios a serem ignorados pelo Git.</li> <li><code>README.md</code>: Este arquivo.</li> </ul> </div> <div> <h2>🚧 Melhorias Planejadas</h2> <ul> <li>🌍 Suporte a múltiplos idiomas para tornar o sistema mais acessível.</li> <li>🤖 Melhorar o processamento de linguagem natural para interpretar comandos mais complexos e flexíveis.</li> <li>📅 Funções extras, como previsão do tempo e gerenciamento de lembretes e alarmes.</li> <li>💱 Expansão das funcionalidades de conversão de moedas para incluir mais detalhes financeiros.</li> <li>📊 Adicionar informações sobre cotações de ações e criptomoedas em tempo real.</li> </ul> </div> <div> <h2>🤝 Contribuição</h2> <p>Contribuições são bem-vindas! Sinta-se à vontade para abrir <strong>issues</strong> e <strong>pull requests</strong>.</p> <ol> <li>Faça um <strong>fork</strong> do projeto.</li> <li>Crie uma nova branch: <code>git checkout -b feature/nova-funcionalidade</code>.</li> <li>Commit suas alterações: <code>git commit -m 'Adiciona nova funcionalidade'</code>.</li> <li>Faça um push para a branch: <code>git push origin feature/nova-funcionalidade</code>.</li> <li>Abra um <strong>pull request</strong>.</li> </ol> </div> <div> <h2>📄 Licença</h2> <p>Este projeto está sob a licença <a href="LICENSE">MIT</a>.</p> </div> <div> <h2>📞 Contato</h2> <p>✉️ Email: <a href="mailto:joaovicttorsilveiramelo@gmail.com">joaovicttorsilveiramelo@gmail.com</a></p> </div>
