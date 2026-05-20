"""
Simple test script for limit order
"""
import sys
from bot.orders import create_order_manager
from bot.client import BinanceClientError
from bot.validators import ValidationError
from bot.logging_config import setup_logging

# Setup logging
setup_logging("INFO")

print("\n" + "="*50)
print("Testing LIMIT BUY Order")
print("="*50 + "\n")

try:
    # Create order manager
    order_manager = create_order_manager()
    
    # Place limit buy order (price set low so it won't execute immediately)
    # Notional value must be >= $50, so 0.002 * 30000 = $60
    order_response = order_manager.place_order(
        symbol="BTCUSDT",
        side="BUY",
        order_type="LIMIT",
        quantity=0.002,
        price=30000  # Set low price so order stays open
    )
    
    print("\n✅ Limit order test PASSED!")
    sys.exit(0)
    
except (ValidationError, BinanceClientError) as e:
    print(f"\n❌ Test FAILED: {e}")
    sys.exit(1)
except Exception as e:
    print(f"\n❌ Unexpected error: {e}")
    sys.exit(1)

# Made with Bob
