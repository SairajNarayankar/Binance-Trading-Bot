# Quick Setup Guide for Binance Futures Trading Bot

## Step-by-Step Setup Instructions

### 1. Get Binance Testnet Credentials

1. Visit [Binance Futures Testnet](https://testnet.binancefuture.com)
2. Click "Register" or "Login" (you can use email or GitHub)
3. Once logged in, go to your account settings
4. Generate API Key and Secret Key
5. **Save these credentials securely** - you'll need them in step 4

### 2. Install Python Dependencies

Open terminal in the `trading_bot` directory and run:

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Linux/Mac:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Configure API Credentials

Create a `.env` file in the `trading_bot` directory:

```bash
# Copy the example file
cp .env.example .env
```

Edit the `.env` file and add your credentials:

```env
BINANCE_API_KEY=your_actual_api_key_here
BINANCE_API_SECRET=your_actual_api_secret_here
```

### 4. Test the Installation

Run a simple command to verify everything works:

```bash
python cli.py balance
```

If successful, you should see your testnet account balance!

### 5. Place Your First Order

Try a small market order:

```bash
python cli.py order --symbol BTCUSDT --side BUY --order-type MARKET --quantity 0.001
```

## Common Issues and Solutions

### Issue: "Module not found" errors
**Solution:** Make sure you're in the `trading_bot` directory and virtual environment is activated:
```bash
cd trading_bot
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac
```

### Issue: "API credentials not found"
**Solution:** Verify your `.env` file exists and contains valid credentials

### Issue: "Import bot.* could not be resolved"
**Solution:** This is a linter warning and can be ignored. The code will run correctly when executed from the project root.

### Issue: Connection errors
**Solution:** 
- Check internet connection
- Verify testnet is accessible: https://testnet.binancefuture.com
- Check firewall settings

## Next Steps

1. Read the full [README.md](README.md) for detailed usage
2. Try different order types (MARKET, LIMIT)
3. Check the `logs/` directory for detailed execution logs
4. Experiment with different trading pairs (ETHUSDT, BNBUSDT, etc.)

## Important Notes

- ⚠️ This bot only works with **TESTNET** - no real money involved
- 📝 All operations are logged in the `logs/` directory
- 🔐 Never commit your `.env` file to version control
- 📊 Check your testnet balance regularly to ensure sufficient funds

## Getting Help

If you encounter issues:
1. Check the log files in `logs/` directory
2. Review error messages carefully
3. Verify API credentials are correct
4. Ensure you're using testnet credentials (not production)

Happy Trading! 🚀