import time
from rich.console import Console
from rich.panel import Panel
from rich.layout import Layout
from rich.live import Live
from rich.text import Text

console = Console()

def run_messenger():
    # Заставка
    console.print("[bold magenta]Запуск zyqvorgram...[/bold magenta]", style="italic")
    time.sleep(1)
    
    messages = [
        ("System", "Добро пожаловать, Zyqvornex!", "cyan"),
        ("System", "Все системы зашифрованы. Протокол активен.", "red")
    ]

    while True:
        # Очистка экрана для красоты
        console.clear()
        
        # Заголовок
        console.print(Panel("[bold white]ZYQVORGRAM[/bold white] [dim]v1.0.4[/dim]", 
                            border_style="magenta", expand=False))
        
        # Вывод истории сообщений
        for sender, text, color in messages:
            console.print(f"[{color}][bold]{sender}:[/bold] {text}[/{color}]")
        
        console.print("\n" + "—" * 30)
        
        # Ввод сообщения
        try:
            user_input = console.input("[bold green]>>> [/bold green]")
            
            if user_input.lower() in ['exit', 'quit', 'выход']:
                console.print("[bold yellow]Сессия завершена.[/bold yellow]")
                break
                
            if user_input:
                messages.append(("Вы", user_input, "blue"))
                
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    run_messenger()