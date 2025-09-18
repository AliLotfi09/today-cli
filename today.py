#!/usr/bin/env python3
import argparse
from datetime import datetime
import jdatetime
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.align import Align
from rich import box

console = Console()

def show_now():
    now = datetime.now()
    table = Table(title="Current Time", box=box.ROUNDED, style="bold cyan")
    table.add_column("Hour", justify="center", style="magenta")
    table.add_column("Minute", justify="center", style="yellow")
    table.add_column("Second", justify="center", style="green")
    table.add_row(f"{now.hour:02d}", f"{now.minute:02d}", f"{now.second:02d}")
    panel = Panel(Align.center(table), title="⏰ Time", border_style="bright_blue")
    console.print(panel)

def show_s():
    today = jdatetime.date.today()
    table = Table(title="Persian Date", box=box.ROUNDED, style="bold cyan")
    table.add_column("Year", justify="center", style="magenta")
    table.add_column("Month", justify="center", style="yellow")
    table.add_column("Day", justify="center", style="green")
    table.add_row(str(today.year), f"{today.month:02d}", f"{today.day:02d}")
    panel = Panel(Align.center(table), title="📅 Persian Calendar", border_style="bright_blue")
    console.print(panel)

def show_m():
    today = datetime.now().date()
    table = Table(title="Gregorian Date", box=box.ROUNDED, style="bold cyan")
    table.add_column("Year", justify="center", style="magenta")
    table.add_column("Month", justify="center", style="yellow")
    table.add_column("Day", justify="center", style="green")
    table.add_row(str(today.year), f"{today.month:02d}", f"{today.day:02d}")
    panel = Panel(Align.center(table), title="🗓️ Gregorian Calendar", border_style="bright_blue")
    console.print(panel)

def main():
    parser = argparse.ArgumentParser(description="A beautiful CLI to show date and time")
    parser.add_argument("command", choices=["now", "s", "m"], 
                       help="Commands: now (time), s (Persian date), m (Gregorian date)")
    
    try:
        args = parser.parse_args()
        if args.command == "now":
            show_now()
        elif args.command == "-s":
            show_s()
        elif args.command == "-m":
            show_m()
    except SystemExit:
        parser.print_help()

if __name__ == "__main__":
    main()