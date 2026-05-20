# Binance Futures Trading Bot

A Python CLI application for placing orders on Binance Futures Testnet (USDT-M). This bot provides a clean, structured interface for executing market and limit orders with comprehensive logging and error handling.

## 🚀 Features

- ✅ Place **Market** and **Limit** orders on Binance Futures Testnet
- ✅ Support for both **BUY** and **SELL** sides
- ✅ Comprehensive input validation
- ✅ Structured logging to file and console
- ✅ Rich CLI output with colored formatting
- ✅ Robust error handling for API and network failures
- ✅ Account balance checking
- ✅ Symbol information lookup

## 📋 Prerequisites

- Python 3.8 or higher
- Binance Futures Testnet account
- API credentials from [Binance Futures Testnet](https://testnet.binancefuture.com)

## 🛠️ Setup

### 1. Clone or Download the Repository

```bash
git clone <your-repository-url>
cd trading_bot
```

### 2. Create Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure API Credentials

Create a `.env` file in the project root:

```bash
# Copy the example file
cp .env.example .env
```

Edit `.env` and add your Binance Futures Testnet credentials:

```env
BINANCE_API_KEY=your_api_key_here
BINANCE_API_SECRET=your_api_secret_here
```

**Important:** Never commit your `.env` file to version control!

## 📖 Usage

### Basic Command Structure

```bash
python cli.py order --symbol <SYMBOL> --side <BUY|SELL> --order-type <MARKET|LIMIT> --quantity <QTY> [--price <PRICE>]
```

### Examples

#### 1. Market Buy Order

```bash
python cli.py order --symbol BTCUSDT --side BUY --order-type MARKET --quantity 0.001
```

#### 2. Market Sell Order

```bash
python cli.py order --symbol BTCUSDT --side SELL --order-type MARKET --quantity 0.001
```

#### 3. Limit Buy Order

```bash
python cli.py order --symbol BTCUSDT --side BUY --order-type LIMIT --quantity 0.001 --price 50000
```

#### 4. Limit Sell Order

```bash
python cli.py order --symbol ETHUSDT --side SELL --order-type LIMIT --quantity 0.01 --price 3000
```

### Additional Commands

#### Check Account Balance

```bash
python cli.py balance
```

#### Get Symbol Information

```bash
python cli.py info --symbol BTCUSDT
```

#### View Help

```bash
python cli.py --help
python cli.py order --help
```

## 📁 Project Structure

```
trading_bot/
├── bot/
│   ├── __init__.py           # Package initialization
│   ├── client.py             # Binance API client wrapper
│   ├── orders.py             # Order placement logic
│   ├── validators.py         # Input validation functions
│   └── logging_config.py     # Logging configuration
├── logs/                     # Log files directory
│   └── trading_bot_*.log     # Timestamped log files
├── cli.py                    # CLI entry point
├── requirements.txt          # Python dependencies
├── .env.example              # Example environment file
├── .gitignore               # Git ignore rules
└── README.md                # This file
```

## 🔍 Component Details

### [`bot/client.py`](bot/client.py)
- Wraps the Binance Futures API client
- Handles authentication and API requests
- Implements error handling for API exceptions
- Provides methods for placing market and limit orders

### [`bot/validators.py`](bot/validators.py)
- Validates all input parameters before API calls
- Checks symbol format, side, order type, quantity, and price
- Raises descriptive errors for invalid inputs

### [`bot/orders.py`](bot/orders.py)
- Orchestrates the order placement workflow
- Coordinates validation, client calls, and response formatting
- Displays rich formatted output for requests and responses

### [`bot/logging_config.py`](bot/logging_config.py)
- Configures structured logging
- Logs to both file and console
- Creates timestamped log files in the `logs/` directory

### [`cli.py`](cli.py)
- Command-line interface using Typer
- Parses user arguments and options
- Handles top-level error catching and exit codes

## 📊 Logging

All operations are logged to timestamped files in the `logs/` directory:

```
logs/
├── trading_bot_20260520_120000.log
├── trading_bot_20260520_130000.log
└── ...
```

Log files include:
- API requests and responses
- Validation results
- Error messages and stack traces
- Order placement confirmations

## ⚠️ Error Handling

The bot handles various error scenarios:

- **Validation Errors**: Invalid parameters (symbol, quantity, price, etc.)
- **API Errors**: Binance API errors (insufficient balance, invalid symbol, etc.)
- **Network Errors**: Connection timeouts, network failures
- **Authentication Errors**: Invalid API credentials

All errors are logged and displayed with clear, actionable messages.

## 🧪 Testing

### Test Cases Executed

1. **Market Buy Order**
   ```bash
   python cli.py order --symbol BTCUSDT --side BUY --order-type MARKET --quantity 0.001
   ```

2. **Market Sell Order**
   ```bash
   python cli.py order --symbol BTCUSDT --side SELL --order-type MARKET --quantity 0.001
   ```

3. **Limit Buy Order**
   ```bash
   python cli.py order --symbol BTCUSDT --side BUY --order-type LIMIT --quantity 0.001 --price 50000
   ```

4. **Limit Sell Order**
   ```bash
   python cli.py order --symbol ETHUSDT --side SELL --order-type LIMIT --quantity 0.01 --price 3000
   ```

### Validation Tests

- Invalid symbol format
- Missing price for LIMIT orders
- Negative quantity
- Invalid side (not BUY/SELL)
- Invalid order type

## 🔐 Security Notes

- API credentials are stored in `.env` file (not committed to git)
- All operations are performed on **TESTNET ONLY**
- No real funds are at risk
- Credentials are loaded via `python-dotenv`

## 🎯 Assumptions

1. **Testnet Environment**: All operations target Binance Futures Testnet
2. **USDT-M Contracts**: Only USDT-margined futures contracts are supported
3. **Minimum Quantities**: User is responsible for respecting minimum order quantities for each symbol
4. **Time in Force**: LIMIT orders use GTC (Good Till Cancel) by default
5. **Python Version**: Python 3.8+ is required for type hints and modern features

## 📝 Dependencies

- `python-binance==1.0.19` - Binance API wrapper
- `python-dotenv==1.0.0` - Environment variable management
- `typer==0.9.0` - CLI framework
- `colorama==0.4.6` - Cross-platform colored terminal output
- `rich==13.7.0` - Rich text and formatting in terminal

## 🐛 Troubleshooting

### Import Errors
If you see import errors, ensure you're in the project root directory and the virtual environment is activated:
```bash
cd trading_bot
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

### API Authentication Errors
- Verify your API credentials in `.env` file
- Ensure you're using Testnet credentials (not production)
- Check that your testnet account is activated

### Connection Errors
- Verify internet connectivity
- Check if Binance Testnet is accessible: https://testnet.binancefuture.com
- Review firewall settings

## 📄 License

This project is created for educational and testing purposes.

## 👤 Author

Trading Bot Developer

## 🙏 Acknowledgments

- Binance for providing the Futures Testnet
- python-binance library maintainers
- Typer and Rich library developers

---

**⚠️ DISCLAIMER**: This bot is for TESTNET use only. Always test thoroughly before using any trading bot with real funds.