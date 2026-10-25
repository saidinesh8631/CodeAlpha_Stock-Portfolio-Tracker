"""
CodeAlpha - Python Programming Internship
Task 2: Stock Portfolio Tracker (Indian MNCs)
"""

import sys

# Ensure UTF-8 output encoding for Indian Rupee symbol (₹) on Windows terminal
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

# Top Indian Multinational Companies (MNCs) with prices in Indian Rupees (INR ₹)
STOCK_PRICES = {
    "TCS": 3920,
    "INFY": 1850,
    "RELIANCE": 2950,
    "HCL TECH": 1720,
    "WIPRO": 540,
    "TATAMOTORS": 940,
    "TECHM": 1580,
    "LT": 3560,
}


def show_available_stocks():
    print("Available Indian MNC stocks and prices (per share in INR):")
    for symbol, price in STOCK_PRICES.items():
        print(f"  {symbol}: ₹{price:,}")
    print()


def get_portfolio_input():
    portfolio = {}
    print("Enter stock symbol and quantity. Type 'done' as symbol to finish.\n")

    while True:
        symbol = input("Stock symbol: ").upper().strip()
        if symbol == "DONE":
            break

        if symbol not in STOCK_PRICES:
            print(f"'{symbol}' not found in stock list. Try again.\n")
            continue

        try:
            quantity = int(input(f"Quantity of {symbol}: ").strip())
            if quantity <= 0:
                print("Quantity must be a positive number.\n")
                continue
        except ValueError:
            print("Please enter a valid whole number.\n")
            continue

        portfolio[symbol] = portfolio.get(symbol, 0) + quantity
        print(f"Added {quantity} share(s) of {symbol}.\n")

    return portfolio


def calculate_total(portfolio):
    breakdown = []
    total = 0
    for symbol, quantity in portfolio.items():
        price = STOCK_PRICES[symbol]
        value = price * quantity
        total += value
        breakdown.append((symbol, quantity, price, value))
    return breakdown, total


def save_to_file(breakdown, total, filename="portfolio_summary.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        f.write("Stock Portfolio Summary (Indian MNCs)\n")
        f.write("=" * 45 + "\n")
        for symbol, quantity, price, value in breakdown:
            f.write(f"{symbol}: {quantity} shares x ₹{price:,} = ₹{value:,}\n")
        f.write("=" * 45 + "\n")
        f.write(f"Total Investment: ₹{total:,}\n")
    print(f"\nPortfolio summary saved to '{filename}'.")


def main():
    print("Welcome to the Indian Stock Portfolio Tracker!\n")
    show_available_stocks()

    portfolio = get_portfolio_input()

    if not portfolio:
        print("No stocks entered. Exiting.")
        return

    breakdown, total = calculate_total(portfolio)

    print("\nPortfolio Summary")
    print("=" * 45)
    for symbol, quantity, price, value in breakdown:
        print(f"{symbol}: {quantity} shares x ₹{price:,} = ₹{value:,}")
    print("=" * 45)
    print(f"Total Investment: ₹{total:,}")

    save_choice = input("\nSave summary to a file? (y/n): ").lower().strip()
    if save_choice == "y":
        save_to_file(breakdown, total)


if __name__ == "__main__":
    main()
