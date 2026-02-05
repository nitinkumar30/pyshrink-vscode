from rich.console import Console
from rich.panel import Panel
from rich.prompt import Confirm, Prompt

console = Console()

def banner():
    console.print(
        Panel.fit(
            "[bold cyan]pyshare[/]\n"
            "Clean it. Zip it. Ship it.",
            title="🚀 Welcome",
        )
    )

def ask_path():
    return Prompt.ask("Enter project root directory")

def ask_confirm(message: str) -> bool:
    return Confirm.ask(message)
