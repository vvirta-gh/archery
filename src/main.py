import os
import sys
import time
from loguru import logger
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt, Confirm


logger.add("logs/app.log", rotation="100 MB", retention="10 days")

console = Console()

# Kaunis menu

def print_main_menu():
    console.print("*** ARCHERY 0.1 ***", style="bold blue")
    console.print("/new - start a new session", style="cyan")
    console.print("/help - show this menu", style="cyan")
    console.print("/list - list all sessions", style="cyan")
    console.print("/user - show user info", style="cyan")
    console.print("/scoreboard - show scoreboard", style="cyan")
    console.print("/settings - show settings", style="cyan")
    console.print("/exit - exit the program", style="cyan")


def main_logic(command: str):
    if command == "/new" or command == "new":
        console.print("Starting a new session...", style="green")
        logger.info("New archery session started")
        time.sleep(1)
        return
    elif command == "/help" or command == "help":
        print_main_menu()
        time.sleep(1)
        return
    elif command == "/list" or command == "list":
        console.print("Listing all sessions...", style="green")
        logger.info("User requested session list")
        time.sleep(1)
        return
    elif command == "/exit" or command == "exit":
        if Confirm.ask("Are you sure you want to exit?"):
            console.print("Exiting...", style="yellow")
            logger.info("Application exited by user")
            time.sleep(1)
            sys.exit(0)
        else:
            console.print("Going back to main menu...", style="blue")
            time.sleep(1)
            return
    else:
        console.print(f"Unknown command: {command}", style="red")
        logger.warning(f"Unknown command entered: {command}")
        return

def main():
    console.print(Panel.fit("*** ARCHERY 0.1 ***", style="bold blue"))
    console.print("Available commands:", style="bold green")
    print_main_menu()

    while True:
        command = Prompt.ask("Enter a command")
        main_logic(command)


if __name__ == "__main__":
    main()
