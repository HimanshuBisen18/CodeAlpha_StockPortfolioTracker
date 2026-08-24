# CodeAlpha_StockPortfolioTracker

A simple **Stock Portfolio Tracker** built in Python as part of the
CodeAlpha Python Programming Internship (Task 2).

## Description

The user enters stock symbols and quantities. Prices are looked up
from a hardcoded dictionary of stock prices. The script calculates
the total investment value and can save the summary to a `.txt` file.

## Features

- Hardcoded dictionary of stock prices (`AAPL`, `TSLA`, `GOOGL`, etc.)
- Accepts multiple stocks in one session, accumulating quantities
- Validates stock symbols and quantity input
- Displays a per-stock and total investment breakdown
- Optionally saves the summary to `portfolio_summary.txt`

## Concepts Used

Dictionaries, input/output, basic arithmetic, file handling

## How to Run

```bash
python3 stock_tracker.py
```

## Example


=== Stock Portfolio Tracker ===

Available stocks and prices (per share):
  AAPL: $180
  TSLA: $250
  ...

Stock symbol: AAPL
Quantity of AAPL: 10
Added 10 share(s) of AAPL.

Stock symbol: done

--- Portfolio Summary ---
AAPL: 10 share(s) x $180 = $1800

Total Investment Value: $1800


## Project Structure


CodeAlpha_StockPortfolioTracker/
├── stock_tracker.py
└── README.md

## Author

Himanshu — CodeAlpha Python Programming Internship
