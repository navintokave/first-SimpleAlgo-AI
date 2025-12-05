import yfinance as yf
import pandas as pd

def sma_strategy_run(symbol: str, fast: int, slow: int):
    df = yf.download(symbol, period="2y", interval="1d")
    df["sma_fast"] = df["Close"].rolling(fast).mean()
    df["sma_slow"] = df["Close"].rolling(slow).mean()

    df["signal"] = (df["sma_fast"] > df["sma_slow"]).astype(int)

    return {
        "symbol": symbol,
        "fast": fast,
        "slow": slow,
        "last_price": float(df["Close"].iloc[-1]),
        "sma_fast": float(df["sma_fast"].iloc[-1]),
        "sma_slow": float(df["sma_slow"].iloc[-1]),
        "signal": int(df["signal"].iloc[-1])
    }
