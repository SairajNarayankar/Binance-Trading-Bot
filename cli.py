"""
Command-line interface for the Binance Futures Trading Bot
Provides user-friendly CLI for placing orders on testnet
"""

import sys
from typing import Optional
import typer
from rich.console import Console
from bot.orders import create_order_manager
from bot.client import BinanceClientError
from bot.validators import ValidationError
from bot.logging_config import setup_logging

# Initialize Typer app
app = typer.Typer(
    name="trading-bot",
    help="Binance Futures Trading Bot - Place orders on testnet",
    add_completion=False
)

console = Console()


@app.command()
def order(
    symbol: str = typer.Option(..., help="Trading pair symbol (e.g., BTCUSDT, ETHUSDT)"),
    side: str = typer.Option(..., help="Order side: BUY or SELL"),
    order_type: str = typer.Option(..., help="Order type: MARKET or LIMIT"),
    quantity: float = typer.Option(..., help="Order quantity (e.g., 0.001 for BTC)"),
    price: Optional[float] = typer.Option(None, help="Limit price (required for LIMIT orders)"),
    log_level: str = typer.Option("INFO", help="Logging level: DEBUG, INFO, WARNING, ERROR, CRITICAL")
):
    """
    Place an order on Binance Futures Testnet
    
    Examples:
    
    Market Buy:
        python cli.py order --symbol BTCUSDT --side BUY --order-type MARKET --quantity 0.001
    
    Market Sell:
        python cli.py order --symbol BTCUSDT --side SELL --order-type MARKET --quantity 0.001
    
    Limit Buy:
        python cli.py order --symbol BTCUSDT --side BUY --order-type LIMIT --quantity 0.001 --price 50000
    
    Limit Sell:
        python cli.py order --symbol ETHUSDT --side SELL --order-type LIMIT --quantity 0.01 --price 3000
    """
    # Setup logging
    setup_logging(log_level)
    
    console.print("\n[bold magenta]╔═══════════════════════════════════════════╗[/bold magenta]")
    console.print("[bold magenta]║  Binance Futures Trading Bot (TESTNET)   ║[/bold magenta]")
    console.print("[bold magenta]╚═══════════════════════════════════════════╝[/bold magenta]\n")
    
    try:
        # Create order manager
        order_manager = create_order_manager()
        
        # Place order
        order_response = order_manager.place_order(
            symbol=symbol,
            side=side,
            order_type=order_type,
            quantity=quantity,
            price=price
        )
        
        # Success - exit with code 0
        sys.exit(0)
        
    except ValidationError as e:
        console.print(f"[bold red]Validation Error:[/bold red] {e}\n")
        sys.exit(1)
    except BinanceClientError as e:
        console.print(f"[bold red]Client Error:[/bold red] {e}\n")
        sys.exit(1)
    except KeyboardInterrupt:
        console.print("\n[yellow]Operation cancelled by user[/yellow]\n")
        sys.exit(130)
    except Exception as e:
        console.print(f"[bold red]Unexpected Error:[/bold red] {e}\n")
        sys.exit(1)


@app.command()
def balance(
    log_level: str = typer.Option("INFO", help="Logging level: DEBUG, INFO, WARNING, ERROR, CRITICAL")
):
    """
    Check account balance on Binance Futures Testnet
    """
    # Setup logging
    setup_logging(log_level)
    
    console.print("\n[bold cyan]Fetching account balance...[/bold cyan]\n")
    
    try:
        from bot.client import BinanceFuturesClient
        
        client = BinanceFuturesClient()
        account = client.get_account_balance()
        
        console.print(f"[bold green]Total Wallet Balance:[/bold green] {account.get('totalWalletBalance', 'N/A')} USDT")
        console.print(f"[bold green]Available Balance:[/bold green] {account.get('availableBalance', 'N/A')} USDT")
        console.print(f"[bold green]Total Unrealized Profit:[/bold green] {account.get('totalUnrealizedProfit', 'N/A')} USDT\n")
        
        sys.exit(0)
        
    except BinanceClientError as e:
        console.print(f"[bold red]Error:[/bold red] {e}\n")
        sys.exit(1)
    except Exception as e:
        console.print(f"[bold red]Unexpected Error:[/bold red] {e}\n")
        sys.exit(1)


@app.command()
def info(
    symbol: str = typer.Option(..., help="Trading pair symbol (e.g., BTCUSDT)"),
    log_level: str = typer.Option("INFO", help="Logging level")
):
    """
    Get trading information for a symbol
    """
    # Setup logging
    setup_logging(log_level)
    
    console.print(f"\n[bold cyan]Fetching info for {symbol}...[/bold cyan]\n")
    
    try:
        from bot.client import BinanceFuturesClient
        
        client = BinanceFuturesClient()
        symbol_info = client.get_symbol_info(symbol.upper())
        
        if symbol_info:
            console.print(f"[bold green]Symbol:[/bold green] {symbol_info.get('symbol')}")
            console.print(f"[bold green]Status:[/bold green] {symbol_info.get('status')}")
            console.print(f"[bold green]Base Asset:[/bold green] {symbol_info.get('baseAsset')}")
            console.print(f"[bold green]Quote Asset:[/bold green] {symbol_info.get('quoteAsset')}\n")
        else:
            console.print(f"[bold red]Symbol {symbol} not found[/bold red]\n")
            sys.exit(1)
        
        sys.exit(0)
        
    except BinanceClientError as e:
        console.print(f"[bold red]Error:[/bold red] {e}\n")
        sys.exit(1)
    except Exception as e:
        console.print(f"[bold red]Unexpected Error:[/bold red] {e}\n")
        sys.exit(1)


def main():
    """Main entry point for the CLI"""
    app()


if __name__ == "__main__":
    main()

# Made with Bob
