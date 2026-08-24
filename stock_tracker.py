

STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 145,
    "MSFT": 410,
    "META": 480,
    "NFLX": 640,
}


def show_available_stocks():
    print("\nAvailable stocks and prices (per share):")
    for symbol, price in STOCK_PRICES.items():
        print(f"  {symbol}: ${price}")


def get_portfolio_input():
    portfolio = {}

    print("\nEnter stock symbol and quantity. Type 'done' as the symbol to finish.")
    while True:
        symbol = input("\nStock symbol: ").strip().upper()

        if symbol == "DONE":
            break

        if symbol not in STOCK_PRICES:
            print(f"'{symbol}' is not in the available stock list. Try again.")
            continue

        quantity_input = input(f"Quantity of {symbol}: ").strip()
        if not quantity_input.isdigit() or int(quantity_input) <= 0:
            print("Please enter a valid positive whole number for quantity.")
            continue

        quantity = int(quantity_input)
        portfolio[symbol] = portfolio.get(symbol, 0) + quantity
        print(f"Added {quantity} share(s) of {symbol}.")

    return portfolio


def calculate_investment(portfolio):
    breakdown = {}
    total = 0
    for symbol, quantity in portfolio.items():
        value = STOCK_PRICES[symbol] * quantity
        breakdown[symbol] = value
        total += value
    return breakdown, total


def save_summary(portfolio, breakdown, total, filename="portfolio_summary.txt"):
    with open(filename, "w") as f:
        f.write("Stock Portfolio Summary\n")
        f.write("=" * 30 + "\n")
        for symbol, quantity in portfolio.items():
            price = STOCK_PRICES[symbol]
            value = breakdown[symbol]
            f.write(f"{symbol}: {quantity} share(s) x ${price} = ${value}\n")
        f.write("=" * 30 + "\n")
        f.write(f"Total Investment: ${total}\n")
    print(f"\nSummary saved to '{filename}'.")


def main():
    print("=== Stock Portfolio Tracker ===")
    show_available_stocks()

    portfolio = get_portfolio_input()

    if not portfolio:
        print("\nNo stocks were added. Exiting.")
        return

    breakdown, total = calculate_investment(portfolio)

    print("\n--- Portfolio Summary ---")
    for symbol, quantity in portfolio.items():
        print(f"{symbol}: {quantity} share(s) x ${STOCK_PRICES[symbol]} = ${breakdown[symbol]}")
    print(f"\nTotal Investment Value: ${total}")

    save_choice = input("\nSave this summary to a file? (y/n): ").strip().lower()
    if save_choice == "y":
        save_summary(portfolio, breakdown, total)


if __name__ == "__main__":
    main()
