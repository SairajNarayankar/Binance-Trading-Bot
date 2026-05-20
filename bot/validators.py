"""
Input validation functions for trading bot
Validates trading parameters before sending to Binance API
"""

import re
from typing import Optional, Tuple
from bot.logging_config import get_logger

logger = get_logger("validators")


class ValidationError(Exception):
    """Custom exception for validation errors"""
    pass


def validate_symbol(symbol: str) -> str:
    """
    Validate trading pair symbol
    
    Args:
        symbol: Trading pair symbol (e.g., BTCUSDT)
    
    Returns:
        Uppercase symbol if valid
    
    Raises:
        ValidationError: If symbol format is invalid
    """
    if not symbol:
        raise ValidationError("Symbol cannot be empty")
    
    symbol = symbol.upper().strip()
    
    # Check if symbol matches expected pattern (letters/numbers ending with USDT)
    if not re.match(r'^[A-Z0-9]+USDT$', symbol):
        raise ValidationError(
            f"Invalid symbol format: {symbol}. "
            "Symbol must end with 'USDT' (e.g., BTCUSDT, ETHUSDT)"
        )
    
    logger.debug(f"Symbol validated: {symbol}")
    return symbol


def validate_side(side: str) -> str:
    """
    Validate order side
    
    Args:
        side: Order side (BUY or SELL)
    
    Returns:
        Uppercase side if valid
    
    Raises:
        ValidationError: If side is not BUY or SELL
    """
    if not side:
        raise ValidationError("Side cannot be empty")
    
    side = side.upper().strip()
    
    if side not in ['BUY', 'SELL']:
        raise ValidationError(
            f"Invalid side: {side}. Must be 'BUY' or 'SELL'"
        )
    
    logger.debug(f"Side validated: {side}")
    return side


def validate_order_type(order_type: str) -> str:
    """
    Validate order type
    
    Args:
        order_type: Order type (MARKET or LIMIT)
    
    Returns:
        Uppercase order type if valid
    
    Raises:
        ValidationError: If order type is not supported
    """
    if not order_type:
        raise ValidationError("Order type cannot be empty")
    
    order_type = order_type.upper().strip()
    
    if order_type not in ['MARKET', 'LIMIT']:
        raise ValidationError(
            f"Invalid order type: {order_type}. Must be 'MARKET' or 'LIMIT'"
        )
    
    logger.debug(f"Order type validated: {order_type}")
    return order_type


def validate_quantity(quantity: float) -> float:
    """
    Validate order quantity
    
    Args:
        quantity: Order quantity
    
    Returns:
        Quantity if valid
    
    Raises:
        ValidationError: If quantity is invalid
    """
    try:
        quantity = float(quantity)
    except (ValueError, TypeError):
        raise ValidationError(f"Invalid quantity: {quantity}. Must be a number")
    
    if quantity <= 0:
        raise ValidationError(
            f"Invalid quantity: {quantity}. Must be greater than 0"
        )
    
    logger.debug(f"Quantity validated: {quantity}")
    return quantity


def validate_price(price: Optional[float], order_type: str) -> Optional[float]:
    """
    Validate order price
    
    Args:
        price: Order price (required for LIMIT orders)
        order_type: Order type (MARKET or LIMIT)
    
    Returns:
        Price if valid, None for MARKET orders
    
    Raises:
        ValidationError: If price is invalid or missing for LIMIT orders
    """
    if order_type == "MARKET":
        if price is not None:
            logger.warning("Price provided for MARKET order will be ignored")
        return None
    
    # For LIMIT orders, price is required
    if price is None:
        raise ValidationError("Price is required for LIMIT orders")
    
    try:
        price = float(price)
    except (ValueError, TypeError):
        raise ValidationError(f"Invalid price: {price}. Must be a number")
    
    if price <= 0:
        raise ValidationError(
            f"Invalid price: {price}. Must be greater than 0"
        )
    
    logger.debug(f"Price validated: {price}")
    return price


def validate_order_params(
    symbol: str,
    side: str,
    order_type: str,
    quantity: float,
    price: Optional[float] = None
) -> Tuple[str, str, str, float, Optional[float]]:
    """
    Validate all order parameters
    
    Args:
        symbol: Trading pair symbol
        side: Order side (BUY/SELL)
        order_type: Order type (MARKET/LIMIT)
        quantity: Order quantity
        price: Order price (required for LIMIT)
    
    Returns:
        Tuple of validated parameters
    
    Raises:
        ValidationError: If any parameter is invalid
    """
    logger.info("Validating order parameters...")
    
    validated_symbol = validate_symbol(symbol)
    validated_side = validate_side(side)
    validated_order_type = validate_order_type(order_type)
    validated_quantity = validate_quantity(quantity)
    validated_price = validate_price(price, validated_order_type)
    
    logger.info("All parameters validated successfully")
    
    return (
        validated_symbol,
        validated_side,
        validated_order_type,
        validated_quantity,
        validated_price
    )

# Made with Bob
