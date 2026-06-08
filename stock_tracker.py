import csv
from datetime import datetime


class StockPortfolioTracker:
    """
    A simple stock portfolio tracker that calculates
    total investment value based on stock quantities.
    """

    STOCK_PRICES = {
        "AAPL": 180,
        "TSLA": 250,
        "GOOGL": 140,
        "MSFT": 420,
        "AMZN": 170
    }

    def __init__(self):
        self.portfolio = {}

    def display_available_stocks(self):
        print("\nAvailable Stocks")
        print("-" * 40)

        for stock, price in self.STOCK_PRICES.items():
            print(f"{stock:<10} ${price}")

        print("-" * 40)

    def add_stock(self):
        stock_name = input(
            "\nEnter stock symbol (AAPL, TSLA, etc.): "
        ).upper()

        if stock_name not in self.STOCK_PRICES:
            print("Invalid stock symbol.")
            return

        try:
            quantity = int(input("Enter quantity: "))

            if quantity <= 0:
                print("Quantity must be greater than zero.")
                return

        except ValueError:
            print("Please enter a valid number.")
            return

        self.portfolio[stock_name] = (
            self.portfolio.get(stock_name, 0) + quantity
        )

        print(
            f"Added {quantity} shares of {stock_name}"
        )

    def calculate_total_value(self):
        total = 0

        for stock, quantity in self.portfolio.items():
            total += (
                self.STOCK_PRICES[stock] * quantity
            )

        return total

    def display_portfolio(self):
        if not self.portfolio:
            print("\nPortfolio is empty.")
            return

        print("\nPortfolio Summary")
        print("-" * 60)

        print(
            f"{'Stock':<10}"
            f"{'Quantity':<10}"
            f"{'Price':<10}"
            f"{'Value':<10}"
        )

        print("-" * 60)

        for stock, quantity in self.portfolio.items():
            price = self.STOCK_PRICES[stock]
            value = price * quantity

            print(
                f"{stock:<10}"
                f"{quantity:<10}"
                f"${price:<9}"
                f"${value:<10}"
            )

        print("-" * 60)
        print(
            f"Total Portfolio Value: "
            f"${self.calculate_total_value():,.2f}"
        )

    def save_to_text(self):
        with open(
            "portfolio_report.txt",
            "w",
            encoding="utf-8"
        ) as file:

            file.write("STOCK PORTFOLIO REPORT\n")
            file.write("=" * 50 + "\n")
            file.write(
                f"Generated: {datetime.now()}\n\n"
            )

            for stock, quantity in self.portfolio.items():
                price = self.STOCK_PRICES[stock]
                value = price * quantity

                file.write(
                    f"{stock} | "
                    f"Qty: {quantity} | "
                    f"Price: ${price} | "
                    f"Value: ${value}\n"
                )

            file.write("\n")
            file.write(
                f"Total Value: "
                f"${self.calculate_total_value():,.2f}"
            )

        print(
            "Portfolio exported to "
            "portfolio_report.txt"
        )

    def save_to_csv(self):
        with open(
            "portfolio_report.csv",
            "w",
            newline="",
            encoding="utf-8"
        ) as file:

            writer = csv.writer(file)

            writer.writerow(
                [
                    "Stock",
                    "Quantity",
                    "Price",
                    "Value"
                ]
            )

            for stock, quantity in self.portfolio.items():
                price = self.STOCK_PRICES[stock]

                writer.writerow(
                    [
                        stock,
                        quantity,
                        price,
                        quantity * price
                    ]
                )

        print(
            "Portfolio exported to "
            "portfolio_report.csv"
        )

    def run(self):
        print("\n📈 STOCK PORTFOLIO TRACKER")

        while True:
            print("\n1. View Stock Prices")
            print("2. Add Stock")
            print("3. View Portfolio")
            print("4. Export to TXT")
            print("5. Export to CSV")
            print("6. Exit")

            choice = input("\nChoose option: ")

            if choice == "1":
                self.display_available_stocks()

            elif choice == "2":
                self.add_stock()

            elif choice == "3":
                self.display_portfolio()

            elif choice == "4":
                self.save_to_text()

            elif choice == "5":
                self.save_to_csv()

            elif choice == "6":
                print("Goodbye!")
                break

            else:
                print("Invalid choice.")


def main():
    tracker = StockPortfolioTracker()
    tracker.run()


if __name__ == "__main__":
    main()
