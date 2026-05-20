@echo off
REM Test script for placing various orders on Binance Futures Testnet (Windows)
REM This script demonstrates all order types and validates the bot functionality

echo ==========================================
echo Binance Futures Trading Bot - Test Suite
echo ==========================================
echo.

REM Check if virtual environment is activated
if not defined VIRTUAL_ENV (
    echo Warning: Virtual environment not activated
    echo Please run: venv\Scripts\activate
    echo.
)

REM Test 1: Check account balance
echo Test 1: Checking account balance...
python cli.py balance
echo.
timeout /t 2 /nobreak >nul

REM Test 2: Market Buy Order
echo Test 2: Placing MARKET BUY order...
python cli.py order --symbol BTCUSDT --side BUY --order-type MARKET --quantity 0.001
echo.
timeout /t 2 /nobreak >nul

REM Test 3: Market Sell Order
echo Test 3: Placing MARKET SELL order...
python cli.py order --symbol BTCUSDT --side SELL --order-type MARKET --quantity 0.001
echo.
timeout /t 2 /nobreak >nul

REM Test 4: Limit Buy Order
echo Test 4: Placing LIMIT BUY order...
python cli.py order --symbol BTCUSDT --side BUY --order-type LIMIT --quantity 0.001 --price 30000
echo.
timeout /t 2 /nobreak >nul

REM Test 5: Limit Sell Order
echo Test 5: Placing LIMIT SELL order...
python cli.py order --symbol BTCUSDT --side SELL --order-type LIMIT --quantity 0.001 --price 80000
echo.
timeout /t 2 /nobreak >nul

REM Test 6: Different symbol - ETH
echo Test 6: Placing MARKET BUY order for ETHUSDT...
python cli.py order --symbol ETHUSDT --side BUY --order-type MARKET --quantity 0.01
echo.
timeout /t 2 /nobreak >nul

REM Test 7: Symbol info
echo Test 7: Getting symbol information...
python cli.py info --symbol BTCUSDT
echo.

echo ==========================================
echo Test suite completed!
echo Check the logs\ directory for detailed logs
echo ==========================================
pause

@REM 
