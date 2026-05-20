"""
Binance Futures API client wrapper
Handles authentication and order placement on Binance Futures Testnet
"""

import os
from typing import Dict, Any, Optional
from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceRequestException
from dotenv import load_dotenv
from bot.logging_config import get_logger

logger = get_logger("client")

# Load environment variables
load_dotenv()


class BinanceClientError(Exception):
    """Custom exception for Binance client errors"""
    pass


class BinanceFuturesClient:
    """
    Wrapper for Binance Futures API client
    Provides methods for placing orders on testnet
    """
    
    def __init__(self, api_key: Optional[str] = None, api_secret: Optional[str] = None):
        """
        Initialize Binance Futures client
        
        Args:
            api_key: Binance API key (defaults to env variable)
            api_secret: Binance API secret (defaults to env variable)
        
        Raises:
            BinanceClientError: If credentials are missing
        """
        self.api_key = api_key or os.getenv("BINANCE_API_KEY")
        self.api_secret = api_secret or os.getenv("BINANCE_API_SECRET")
        
        if not self.api_key or not self.api_secret:
            raise BinanceClientError(
                "API credentials not found. Please set BINANCE_API_KEY and "
                "BINANCE_API_SECRET in .env file or pass them as arguments."
            )
        
        try:
            # Initialize client with testnet configuration
            self.client = Client(
                api_key=self.api_key,
                api_secret=self.api_secret,
                testnet=True
            )
            
            # Set to use Futures API
            self.client.API_URL = 'https://testnet.binancefuture.com'
            
            logger.info("Binance Futures client initialized successfully (TESTNET)")
            
            # Test connection
            self._test_connection()
            
        except Exception as e:
            logger.error(f"Failed to initialize Binance client: {e}")
            raise BinanceClientError(f"Client initialization failed: {e}")
    
    def _test_connection(self) -> None:
        """
        Test API connection and credentials
        
        Raises:
            BinanceClientError: If connection test fails
        """
        try:
            # Test connectivity
            self.client.futures_ping()
            logger.info("API connection test successful")
            
            # Test authentication by getting account info
            account = self.client.futures_account()
            logger.info(f"Account authenticated. Balance: {account.get('totalWalletBalance', 'N/A')} USDT")
            
        except BinanceAPIException as e:
            logger.error(f"API authentication failed: {e}")
            raise BinanceClientError(f"Authentication failed: {e.message}")
        except Exception as e:
            logger.error(f"Connection test failed: {e}")
            raise BinanceClientError(f"Connection test failed: {e}")
    
    def place_market_order(
        self,
        symbol: str,
        side: str,
        quantity: float
    ) -> Dict[str, Any]:
        """
        Place a market order on Binance Futures
        
        Args:
            symbol: Trading pair (e.g., BTCUSDT)
            side: Order side (BUY or SELL)
            quantity: Order quantity
        
        Returns:
            Order response from Binance API
        
        Raises:
            BinanceClientError: If order placement fails
        """
        logger.info(f"Placing MARKET order: {side} {quantity} {symbol}")
        
        try:
            # Log request details
            logger.debug(f"Request - Symbol: {symbol}, Side: {side}, Quantity: {quantity}, Type: MARKET")
            
            # Place market order
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type='MARKET',
                quantity=quantity
            )
            
            # Log response
            logger.info(f"Order placed successfully. Order ID: {order.get('orderId')}")
            logger.debug(f"Full response: {order}")
            
            return order
            
        except BinanceAPIException as e:
            error_msg = f"Binance API error: {e.message} (Code: {e.code})"
            logger.error(error_msg)
            raise BinanceClientError(error_msg)
        except BinanceRequestException as e:
            error_msg = f"Request failed: {e}"
            logger.error(error_msg)
            raise BinanceClientError(error_msg)
        except Exception as e:
            error_msg = f"Unexpected error placing market order: {e}"
            logger.error(error_msg)
            raise BinanceClientError(error_msg)
    
    def place_limit_order(
        self,
        symbol: str,
        side: str,
        quantity: float,
        price: float
    ) -> Dict[str, Any]:
        """
        Place a limit order on Binance Futures
        
        Args:
            symbol: Trading pair (e.g., BTCUSDT)
            side: Order side (BUY or SELL)
            quantity: Order quantity
            price: Limit price
        
        Returns:
            Order response from Binance API
        
        Raises:
            BinanceClientError: If order placement fails
        """
        logger.info(f"Placing LIMIT order: {side} {quantity} {symbol} @ {price}")
        
        try:
            # Log request details
            logger.debug(
                f"Request - Symbol: {symbol}, Side: {side}, "
                f"Quantity: {quantity}, Price: {price}, Type: LIMIT"
            )
            
            # Place limit order
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type='LIMIT',
                timeInForce='GTC',  # Good Till Cancel
                quantity=quantity,
                price=price
            )
            
            # Log response
            logger.info(f"Order placed successfully. Order ID: {order.get('orderId')}")
            logger.debug(f"Full response: {order}")
            
            return order
            
        except BinanceAPIException as e:
            error_msg = f"Binance API error: {e.message} (Code: {e.code})"
            logger.error(error_msg)
            raise BinanceClientError(error_msg)
        except BinanceRequestException as e:
            error_msg = f"Request failed: {e}"
            logger.error(error_msg)
            raise BinanceClientError(error_msg)
        except Exception as e:
            error_msg = f"Unexpected error placing limit order: {e}"
            logger.error(error_msg)
            raise BinanceClientError(error_msg)
    
    def get_account_balance(self) -> Dict[str, Any]:
        """
        Get account balance information
        
        Returns:
            Account balance data
        """
        try:
            account = self.client.futures_account()
            logger.debug(f"Account balance retrieved: {account.get('totalWalletBalance')} USDT")
            return account
        except Exception as e:
            logger.error(f"Failed to get account balance: {e}")
            raise BinanceClientError(f"Failed to get account balance: {e}")
    
    def get_symbol_info(self, symbol: str) -> Optional[Dict[str, Any]]:
        """
        Get trading rules and information for a symbol
        
        Args:
            symbol: Trading pair symbol
        
        Returns:
            Symbol information or None if not found
        """
        try:
            exchange_info = self.client.futures_exchange_info()
            for s in exchange_info['symbols']:
                if s['symbol'] == symbol:
                    logger.debug(f"Symbol info retrieved for {symbol}")
                    return s
            logger.warning(f"Symbol {symbol} not found")
            return None
        except Exception as e:
            logger.error(f"Failed to get symbol info: {e}")
            return None
