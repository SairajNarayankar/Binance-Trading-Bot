# 🐍 Binance Futures Trading Bot

<div align="center">

![TradingBot Banner](https://img.shields.io/badge/Binance%20Futures-Trading%20Bot-F0B90B?style=for-the-badge&logo=binance&logoColor=black)
![Python](https://img.shields.io/badge/Python%203.8+-Powered-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Typer CLI](https://img.shields.io/badge/Typer-CLI%20Framework-009688?style=for-the-badge&logo=python&logoColor=white)
![Testnet](https://img.shields.io/badge/Binance%20Testnet-Safe%20%26%20Sandboxed-green?style=for-the-badge)
![License](https://img.shields.io/badge/License-Educational-orange?style=for-the-badge)

**A modular, production-grade Python CLI tool for placing MARKET and LIMIT orders on Binance Futures Testnet — with input validation, rich terminal output, structured logging, and a clean layered architecture.**

📖 **[How It Works](#-architecture)** &nbsp;|&nbsp; 🚀 **[Quick Start](#️-setup)** &nbsp;|&nbsp; 🧪 **[Testing](#-testing)**

</div>

---

## 🏆 Project Highlights

> Built as a complete, submission-ready trading bot with a focus on **code quality**, **error resilience**, and **developer experience** — all within a single focused Python CLI application.
>
> All operations run exclusively on **Binance Futures Testnet** — no real funds are ever at risk.

<div align="center">

![Binance](https://img.shields.io/badge/Exchange-Binance%20Futures%20Testnet-F0B90B?style=for-the-badge&logo=binance)
![Status](https://img.shields.io/badge/Status-Complete%20%E2%9C%85-brightgreen?style=for-the-badge)

</div>

---

## ✨ What is This Bot?

This is a **fully structured, CLI-driven trading bot** that interfaces with the Binance Futures Testnet API. It allows you to place real-time MARKET and LIMIT orders via simple terminal commands, with comprehensive validation, rich output formatting, and full audit logging.

Whether you're learning algorithmic trading, preparing for a technical assessment, or prototyping a futures strategy, this bot gives you a clean, battle-tested starting point.

---

## 🎯 Features

| Feature | Description |
|---|---|
| 📈 **Market Orders** | Instantly execute BUY or SELL at current market price |
| 📉 **Limit Orders** | Set a target price for BUY or SELL with GTC time-in-force |
| ✅ **Input Validation** | Validates symbol, side, order type, quantity, and price before any API call |
| 🎨 **Rich Terminal Output** | Color-coded panels, formatted tables, and progress indicators via `rich` |
| 📋 **Structured Logging** | Timestamped log files capturing every request, response, and error |
| 💰 **Balance Checker** | View your Testnet USDT wallet balance with one command |
| 🔍 **Symbol Info Lookup** | Fetch trading pair metadata directly from the CLI |
| 🧪 **Built-in Test Scripts** | Automated test scripts for both Linux/Mac and Windows |
| 🏗️ **Modular Architecture** | Clean separation across client, validation, orchestration, and CLI layers |
| 🔒 **Secure by Design** | Credentials loaded via `.env` — never hardcoded or committed |

---

## 🖥️ CLI Demo

```
# Check your testnet account balance
python cli.py balance

# Place a market buy order
python cli.py order --symbol BTCUSDT --side BUY --order-type MARKET --quantity 0.001

# Place a limit sell order
python cli.py order --symbol ETHUSDT --side SELL --order-type LIMIT --quantity 0.01 --price 3000

# Look up symbol details
python cli.py info --symbol BTCUSDT
```

**Sample Test Results (Testnet):**

| Test | Symbol | Type | Qty | Price | Order ID | Status |
|---|---|---|---|---|---|---|
| Market BUY | BTCUSDT | MARKET | 0.001 | — | 13167819799 | ✅ NEW |
| Limit BUY | BTCUSDT | LIMIT | 0.002 | 30000 | 13167823908 | ✅ NEW |
| Account Balance | — | — | — | — | — | 5000 USDT |

---

## 🏗️ Architecture

```
CLI User Input (cli.py)
        │
        ▼
 Input Validation (bot/validators.py)
        │
        ▼
 Order Orchestration (bot/orders.py)
        │
        ├── Logging (bot/logging_config.py) ──► logs/trading_bot_*.log
        │
        ▼
 Binance API Client (bot/client.py)
        │
        ▼
 Binance Futures Testnet API
        │
        ▼
Rich-Formatted Response → Terminal
```

**Exchange:** Binance Futures Testnet (`https://testnet.binancefuture.com`)  
**Contract Type:** USDT-M Perpetual Futures  
**Default Time-in-Force:** GTC (Good Till Cancel) for LIMIT orders

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **Language** | Python 3.8+ |
| **CLI Framework** | Typer 0.9.0 |
| **Terminal UI** | Rich 13.7.0 |
| **Exchange API** | python-binance 1.0.19 |
| **Color Output** | Colorama 0.4.6 |
| **Config Management** | python-dotenv 1.0.0 |
| **Logging** | Python `logging` (stdlib) |
| **Testing** | Shell scripts + Python test files |

---

## 🚀 Setup

### Prerequisites
- [Python 3.8+](https://python.org)
- A [Binance Futures Testnet](https://testnet.binancefuture.com) account
- Testnet API Key + Secret (free — no real money needed)

### 1. Clone the Repository

```bash
git clone https://github.com/SairajNarayankar/Binance-Trading-Bot.git
cd Binance-Trading-Bot
```

### 2. Create a Virtual Environment

```bash
# Linux / Mac
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Your API Credentials

```bash
# Copy the example file
cp .env.example .env
```

Open `.env` and fill in your Binance Testnet credentials:

```env
BINANCE_API_KEY=your_testnet_api_key_here
BINANCE_API_SECRET=your_testnet_api_secret_here
```

> ⚠️ **Never commit your `.env` file.** It is already listed in `.gitignore`.

### 5. Verify the Connection

```bash
python cli.py balance
```

---

## 📖 Usage

### Command Reference

```bash
python cli.py order --symbol <SYMBOL> \
                    --side <BUY|SELL> \
                    --order-type <MARKET|LIMIT> \
                    --quantity <QTY> \
                    [--price <PRICE>]   # Required for LIMIT orders only
```

### Examples

#### Market Buy Order
```bash
python cli.py order --symbol BTCUSDT --side BUY --order-type MARKET --quantity 0.001
```

#### Market Sell Order
```bash
python cli.py order --symbol BTCUSDT --side SELL --order-type MARKET --quantity 0.001
```

#### Limit Buy Order
```bash
python cli.py order --symbol BTCUSDT --side BUY --order-type LIMIT --quantity 0.001 --price 50000
```

#### Limit Sell Order
```bash
python cli.py order --symbol ETHUSDT --side SELL --order-type LIMIT --quantity 0.01 --price 3000
```

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

---

## 📁 Project Structure

```
Binance-Trading-Bot/
├── bot/
│   ├── __init__.py           # Package initialization
│   ├── client.py             # Binance API client wrapper
│   ├── orders.py             # Order orchestration logic
│   ├── validators.py         # Input validation functions
│   └── logging_config.py     # Logging configuration
├── logs/                     # Auto-generated timestamped log files
│   └── trading_bot_*.log
├── sample_logs/              # Example log files for reference
│   ├── market_order_example.log
│   ├── limit_order_example.log
│   └── README.md
├── cli.py                    # CLI entry point (Typer)
├── requirements.txt          # Python dependencies
├── test_market_order.py      # Automated market order test
├── test_limit_order.py       # Automated limit order test
├── test_orders.sh            # Linux/Mac test suite
├── test_orders.bat           # Windows test suite
├── .env.example              # Credentials template
├── .gitignore                # Excludes .env, logs, venv
├── SETUP_GUIDE.md            # Quick setup instructions
├── PROJECT_SUMMARY.md        # Full project evaluation summary
└── README.md                 # This file
```

---

## 🔍 Component Details

### `bot/client.py`
- Wraps the `python-binance` Futures API client
- Handles authentication, base URL config, and API requests
- Provides clean methods for placing market and limit orders
- Catches and re-raises Binance API exceptions with context

### `bot/validators.py`
- Validates all user inputs before any API call is made
- Enforces correct symbol format, side (BUY/SELL), order type, quantity, and price rules
- Returns descriptive, user-friendly error messages on invalid input

### `bot/orders.py`
- Orchestrates the full order placement workflow
- Coordinates validation → client call → response parsing → rich output
- Displays formatted request summary and response table via `rich`

### `bot/logging_config.py`
- Configures dual logging: timestamped file + console output
- Creates a new log file per session under `logs/`
- Captures API requests, responses, validation outcomes, and errors

### `cli.py`
- CLI interface built with [Typer](https://typer.tiangolo.com/)
- Parses all arguments and options with type safety
- Handles top-level exceptions and returns appropriate exit codes

---

## 📊 Logging

Every session writes to a new timestamped log file:

```
logs/
├── trading_bot_20260520_120000.log
├── trading_bot_20260520_130000.log
└── ...
```

Logs capture:
- All API requests (symbol, side, type, quantity, price)
- Full API responses (Order ID, status, executed qty, avg price)
- Validation pass/fail results
- Error messages with complete stack traces
- Order confirmations and balance check results

---

## ⚠️ Error Handling

The bot gracefully handles all common failure scenarios:

| Error Type | Example | Behavior |
|---|---|---|
| **Validation Error** | Negative quantity, missing price | Descriptive error, no API call made |
| **API Error** | Insufficient balance, invalid pair | Binance error code + message displayed |
| **Network Error** | Timeout, connection refused | Retry guidance and error logged |
| **Auth Error** | Wrong API key/secret | Clear credential error with troubleshooting tip |

---

## 🧪 Testing

### Automated Test Scripts

**Linux / Mac:**
```bash
chmod +x test_orders.sh
./test_orders.sh
```

**Windows:**
```bat
test_orders.bat
```

**Python Test Files:**
```bash
python test_market_order.py
python test_limit_order.py
```

### Validation Test Cases

| Scenario | Input | Expected Result |
|---|---|---|
| Invalid symbol | `INVALIDPAIR` | Validation error |
| Missing price on LIMIT | No `--price` flag | Error: price required |
| Negative quantity | `--quantity -1` | Error: must be positive |
| Wrong side | `--side HOLD` | Error: must be BUY or SELL |
| Wrong order type | `--order-type STOP` | Error: must be MARKET or LIMIT |

---

## 🔐 Security

- ✅ API credentials stored in `.env` file — never hardcoded
- ✅ `.env` excluded from git via `.gitignore`
- ✅ All operations run on **Testnet only** — no production keys needed
- ✅ Credentials loaded at runtime via `python-dotenv`
- ✅ No credentials printed to terminal or logged to files

---

## 📝 Assumptions

1. **Testnet Environment** — All operations target `https://testnet.binancefuture.com` exclusively
2. **USDT-M Contracts** — Only USDT-margined perpetual futures are supported
3. **Minimum Notional** — Orders must meet the $50 minimum (quantity × price ≥ 50 USDT)
4. **Time in Force** — LIMIT orders default to GTC (Good Till Cancel)
5. **Python Version** — Python 3.8+ required for type hints and f-string features

---

## 🐛 Troubleshooting

### Import Errors
Ensure you are in the project root with your virtual environment active:
```bash
cd Binance-Trading-Bot
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

### API Authentication Errors
- Double-check credentials in your `.env` file
- Confirm you are using **Testnet** keys (not production Binance keys)
- Verify your Testnet account is activated at [testnet.binancefuture.com](https://testnet.binancefuture.com)

### Connection Errors
- Verify internet connectivity
- Confirm Binance Testnet is reachable: [https://testnet.binancefuture.com](https://testnet.binancefuture.com)
- Review any firewall or proxy restrictions on your network

---

## 📊 Code Quality Metrics

| Metric | Value |
|---|---|
| **Total Source Files** | 14 |
| **Lines of Code** | ~1,500+ |
| **Language** | Python 88.9%, Shell 5.4%, Batchfile 5.7% |
| **Architecture Layers** | 5 (Client, Validation, Orchestration, Presentation, Logging) |
| **Design Patterns Used** | Factory, Strategy, Facade, Singleton |
| **Documentation Files** | 4 comprehensive Markdown guides |
| **Code Style** | PEP 8 compliant, fully type-hinted |

---

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Open an issue for bugs or feature requests
- Submit a pull request with improvements
- Suggest new order types, exchanges, or CLI commands

---

## 📄 License

This project is created for **educational and testing purposes**. See the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Sairaj Narayankar**

[![GitHub](https://img.shields.io/badge/GitHub-SairajNarayankar-181717?style=for-the-badge&logo=github)](https://github.com/SairajNarayankar)

---

<div align="center">

Built with ❤️ for algorithmic trading education &nbsp;|&nbsp; Powered by **python-binance** &nbsp;|&nbsp; Runs on **Binance Futures Testnet**

📈 *Trade smart. Test first. Never risk real funds without thorough testing.*

> ⚠️ **DISCLAIMER**: This bot is for **TESTNET use only**. Always test thoroughly before using any trading bot with real funds. The author is not responsible for any financial losses.

</div>
