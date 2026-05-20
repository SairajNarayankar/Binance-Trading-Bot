"""
Simple test script for market order
"""
import sys
from bot.orders import create_order_manager
from bot.client import BinanceClientError
from bot.validators import ValidationError
from bot.logging_config import setup_logging

# Setup logging
setup_logging("INFO")

print("\n" + "="*50)
print("Testing MARKET BUY Order")
print("="*50 + "\n")

try:
    # Create order manager
    order_manager = create_order_manager()
    
    # Place market buy order
    order_response = order_manager.place_order(
        symbol="BTCUSDT",
        side="BUY",
        order_type="MARKET",
        quantity=0.001,
        price=None
    )
    
    print("\n✅ Market order test PASSED!")
    sys.exit(0)
    
except (ValidationError, BinanceClientError) as e:
    print(f"\n❌ Test FAILED: {e}")
    sys.exit(1)
except Exception as e:
    print(f"\n❌ Unexpected error: {e}")
    sys.exit(1)

# Made with Bob
