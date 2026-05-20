"""
Order placement logic and orchestration
Coordinates validation, client calls, and response formatting
"""

from typing import Dict, Any, Optional
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from bot.client import BinanceFuturesClient, BinanceClientError
from bot.validators import validate_order_params, ValidationError
from bot.logging_config import get_logger

logger = get_logger("orders")
console = Console()


class OrderManager:
    """
    Manages order placement workflow
    Handles validation, execution, and result presentation
    """
    
    def __init__(self, client: BinanceFuturesClient):
        """
        Initialize order manager
        
        Args:
            client: Initialized Binance Futures client
        """
        self.client = client
        logger.info("OrderManager initialized")
    
    def place_order(
        self,
        symbol: str,
        side: str,
        order_type: str,
        quantity: float,
        price: Optional[float] = None
    ) -> Dict[str, Any]:
        """
        Place an order with validation and error handling
        
        Args:
            symbol: Trading pair symbol
            side: Order side (BUY/SELL)
            order_type: Order type (MARKET/LIMIT)
            quantity: Order quantity
            price: Order price (required for LIMIT)
        
        Returns:
            Order response from Binance API
        
        Raises:
            ValidationError: If parameters are invalid
            BinanceClientError: If order placement fails
        """
        # Display order request summary
        self._display_order_request(symbol, side, order_type, quantity, price)
        
        try:
            # Validate all parameters
            validated_params = validate_order_params(
                symbol, side, order_type, quantity, price
            )
            symbol, side, order_type, quantity, price = validated_params
            
            logger.info(f"Placing {order_type} order...")
            
            # Place order based on type
            if order_type == "MARKET":
                order_response = self.client.place_market_order(
                    symbol=symbol,
                    side=side,
                    quantity=quantity
                )
            else:  # LIMIT
                order_response = self.client.place_limit_order(
                    symbol=symbol,
                    side=side,
                    quantity=quantity,
                    price=price
                )
            
            # Display order response
            self._display_order_response(order_response, success=True)
            
            return order_response
            
        except ValidationError as e:
            logger.error(f"Validation error: {e}")
            self._display_error(f"Validation Error: {e}")
            raise
        except BinanceClientError as e:
            logger.error(f"Order placement failed: {e}")
            self._display_error(f"Order Failed: {e}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            self._display_error(f"Unexpected Error: {e}")
            raise
    
    def _display_order_request(
        self,
        symbol: str,
        side: str,
        order_type: str,
        quantity: float,
        price: Optional[float]
    ) -> None:
        """
        Display order request summary in a formatted table
        
        Args:
            symbol: Trading pair symbol
            side: Order side
            order_type: Order type
            quantity: Order quantity
            price: Order price (optional)
        """
        console.print("\n[bold cyan]═══ Order Request Summary ═══[/bold cyan]")
        
        table = Table(show_header=False, box=None, padding=(0, 2))
        table.add_column("Parameter", style="bold yellow")
        table.add_column("Value", style="white")
        
        table.add_row("Symbol", symbol)
        table.add_row("Side", side)
        table.add_row("Type", order_type)
        table.add_row("Quantity", str(quantity))
        
        if price is not None:
            table.add_row("Price", str(price))
        
        console.print(table)
        console.print()
    
    def _display_order_response(
        self,
        order: Dict[str, Any],
        success: bool = True
    ) -> None:
        """
        Display order response in a formatted table
        
        Args:
            order: Order response from Binance API
            success: Whether the order was successful
        """
        if success:
            console.print("[bold green]✓ Order Placed Successfully![/bold green]\n")
        
        table = Table(show_header=False, box=None, padding=(0, 2))
        table.add_column("Field", style="bold cyan")
        table.add_column("Value", style="white")
        
        # Key fields to display
        fields = [
            ("Order ID", "orderId"),
            ("Symbol", "symbol"),
            ("Side", "side"),
            ("Type", "type"),
            ("Status", "status"),
            ("Quantity", "origQty"),
            ("Executed Qty", "executedQty"),
            ("Price", "price"),
            ("Avg Price", "avgPrice"),
            ("Time in Force", "timeInForce"),
            ("Update Time", "updateTime"),
        ]
        
        for field_name, field_key in fields:
            value = order.get(field_key)
            if value is not None and value != "":
                # Format timestamp if it's updateTime
                if field_key == "updateTime":
                    from datetime import datetime
                    value = datetime.fromtimestamp(value / 1000).strftime("%Y-%m-%d %H:%M:%S")
                table.add_row(field_name, str(value))
        
        console.print(table)
        console.print()
        
        # Display success message with order ID
        order_id = order.get("orderId", "N/A")
        status = order.get("status", "UNKNOWN")
        
        message = f"Order #{order_id} - Status: {status}"
        console.print(Panel(
            message,
            style="bold green" if success else "bold red",
            border_style="green" if success else "red"
        ))
        console.print()
    
    def _display_error(self, error_message: str) -> None:
        """
        Display error message in a formatted panel
        
        Args:
            error_message: Error message to display
        """
        console.print()
        console.print(Panel(
            f"[bold red]✗ {error_message}[/bold red]",
            title="Error",
            border_style="red"
        ))
        console.print()


def create_order_manager() -> OrderManager:
    """
    Factory function to create an OrderManager instance
    
    Returns:
        Initialized OrderManager
    
    Raises:
        BinanceClientError: If client initialization fails
    """
    try:
        client = BinanceFuturesClient()
        return OrderManager(client)
    except BinanceClientError as e:
        logger.error(f"Failed to create order manager: {e}")
        raise

# Made with Bob
