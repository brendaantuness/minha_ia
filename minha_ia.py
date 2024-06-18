# Rodar esse código no google Colab https://colab.research.google.com/

!pip install -q google-generativeai
!pip install rich
import google.generativeai as genai
from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table

# Configuração da chave de API
# Gerar chave https://aistudio.google.com/app/apikey gerar com um dos colegas
GOOGLE_GEMINI_API_KEY = 'minha-chave'  # Substitua por sua chave de API válida

# Configuração do cliente Gemini
genai.configure(api_key=GOOGLE_GEMINI_API_KEY)

# Definindo o modelo do Gemini
try:
    model = genai.GenerativeModel("gemini-1.5-pro-latest")
except Exception as e:
    print(f"Erro ao configurar o modelo: {e}")
    exit()

# Iniciando a sessão de chat
try:
    chat = model.start_chat(history=[])
except Exception as e:
    print(f"Erro ao iniciar a sessão de chat: {e}")
    exit()

# Prompt inicial não exibido ao usuário, para orientar as respostas do modelo
initial_prompt = "Você é um assistente amigável que ajuda as pessoas a aprenderem Power BI de maneira clara e acolhedora."

# Enviando o prompt inicial para balizar a resposta do modelo
try:
    chat.send_message(initial_prompt)
except Exception as e:
    print(f"Erro ao enviar o prompt inicial: {e}")
    exit()

# Inicializando o console para saída de texto estilizada
console = Console()

# Função para exibir o histórico de conversas em uma tabela
def print_chat_history(history):
    """Exibe o histórico de conversas em formato de tabela.
    
    Args:
        history (list): Lista de tuplas contendo as mensagens do usuário e as respostas do assistente.
    """
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Usuário", style="dim")
    table.add_column("Assistente")
    
    for i, (user_input, response) in enumerate(history):
        table.add_row(f"[green]{user_input}[/green]", f"[blue]{response}[/blue]")
    
    console.print(table)

# Histórico de conversas
chat_history = []

# Mensagem inicial de boas-vindas
console.print("[bold yellow]Bem-vindo! Estou aqui para te ajudar com suas dúvidas sobre Python.[/bold yellow]")
console.print("Digite [bold magenta]'fim'[/bold magenta] a qualquer momento para encerrar a conversa.", style="bold yellow")

# Loop de interação com o usuário
while True:
    user_input = Prompt.ask("\n[bold cyan]Como posso te ajudar hoje?[/bold cyan]")

    if user_input.strip().lower() == "fim":
        console.print("[bold red]Conversa encerrada. Até a próxima![/bold red]")
        break
    
    if not user_input.strip():
        console.print("[bold red]Por favor, digite uma pergunta ou comando válido.[/bold red]")
        continue
    
    try:
        # Enviando a mensagem do usuário ao modelo e recebendo a resposta
        response = chat.send_message(user_input)
        response_text = response.text.strip()
    except Exception as e:
        console.print(f"[bold red]Erro ao processar a mensagem: {e}[/bold red]")
        continue
    
    # Atualizando o histórico de conversas
    chat_history.append((user_input, response_text))
    
    # Limpando o console para exibir o histórico atualizado
    console.clear()
    print_chat_history(chat_history)
