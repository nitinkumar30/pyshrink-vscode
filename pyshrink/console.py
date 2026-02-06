"""
Console UI using Rich library
"""

try:
    from rich.console import Console
    from rich.panel import Panel
    from rich.prompt import Prompt, Confirm
    from rich.table import Table
    RICH_AVAILABLE = True
except ImportError:
    RICH_AVAILABLE = False
    print("⚠️  Rich library not installed. Using plain output.")
    print("   Install with: pip install rich")

class ConsoleUI:
    """Console UI handler"""
    
    def __init__(self):
        if RICH_AVAILABLE:
            self.console = Console()
        else:
            self.console = None
    
    def print_banner(self):
        """Print application banner"""
        if self.console:
            self.console.print(Panel.fit(
                "🚀 [bold cyan]PyShrink[/bold cyan] - Python Project Cleaner",
                border_style="cyan"
            ))
        else:
            print("\n" + "="*50)
            print("🚀 PyShrink - Python Project Cleaner")
            print("="*50 + "\n")
    
    def print_success(self, message):
        """Print success message"""
        if self.console:
            self.console.print(f"✅ [green]{message}[/green]")
        else:
            print(f"✅ {message}")
    
    def print_error(self, message):
        """Print error message"""
        if self.console:
            self.console.print(f"❌ [red]{message}[/red]")
        else:
            print(f"❌ {message}")
    
    def print_warning(self, message):
        """Print warning message"""
        if self.console:
            self.console.print(f"⚠️  [yellow]{message}[/yellow]")
        else:
            print(f"⚠️  {message}")
    
    def print_info(self, message):
        """Print info message"""
        if self.console:
            self.console.print(f"ℹ️  [cyan]{message}[/cyan]")
        else:
            print(f"ℹ️  {message}")
    
    def ask_yes_no(self, question):
        """Ask yes/no question"""
        if self.console:
            return Confirm.ask(question)
        else:
            while True:
                response = input(f"{question} [y/n]: ").lower()
                if response in ['y', 'yes']:
                    return True
                elif response in ['n', 'no']:
                    return False
                print("Please enter 'y' or 'n'")
    
    def ask_input(self, prompt_text):
        """Ask for user input"""
        if self.console:
            return Prompt.ask(prompt_text)
        else:
            return input(f"{prompt_text}: ")
