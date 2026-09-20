class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        """Returns the total calculated from coins inserted."""
        print("Please insert coins.")
        large_dollars = int(input("how many large dollars?: ")) * 1.00
        half_dollars = int(input("how many half dollars?: ")) * 0.50
        quarters = int(input("how many quarters?: ")) * 0.25
        nickels = int(input("how many nickels?: ")) * 0.05
        pennies = int(input("how many pennies?: ")) * 0.01
        total = large_dollars + half_dollars + quarters + nickels + pennies
        return total

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient."""
        if coins >= cost:
            change = round(coins - cost, 2)
            if change > 0:
                print(f"Here is ${change} in change.")
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            return False