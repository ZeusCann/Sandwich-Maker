### Data ###

recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24,  ## ounces
}


### Complete functions ###

class SandwichMachine:

    def __init__(self, machine_resources):
        """Receives resources as input.
           Hint: bind input variable to self variable"""
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        if ingredients["bread"] > self.machine_resources["bread"]:
            print("Sorry, there is not enough bread")
            return False
        elif ingredients["ham"] > self.machine_resources["ham"]:
            print("Sorry, there is not enough ham")
            return False
        elif ingredients["cheese"] > self.machine_resources["cheese"]:
            print("Sorry, there is not enough cheese")
            return False
        else:
            return True

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        print("Please insert coins.")
        dollars = float(input("How many dollars?: "))
        half_dollars = float(input("How many half dollars?: ")) * 0.5
        quarters = float(input("How many quarters?: ")) * 0.25
        nickels = float(input("How many nickels?: ")) * 0.05
        payment = dollars + half_dollars + quarters + nickels
        return payment

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if coins < cost:
            print("Sorry, there is not enough money..")
            return False

        change = coins - cost
        print(f"Here's your change: ${change:.2f}")
        return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""
        for item, amount in order_ingredients.items():
            self.machine_resources[item] -= amount
        print(f"{sandwich_size} sandwich is ready. Bon Appetit!")

    def report(self):
        print(f"Bread: {resources["bread"]}\n"
              f"Ham: {resources["ham"]}\n"
              f"Cheese: {resources["cheese"]}\n")

### Make an instance of SandwichMachine class and write the rest of the codes ###
order = SandwichMachine(resources)
while True:
    ordering = input(
        "What would you like? (small/medium/large/off/ report): ").lower()

    if ordering == "off":
        break

    if ordering == "report":
        order.report()
        continue

    if ordering not in recipes:
        # Ignore unknown input and reprompt
        continue

    recipe = recipes[ordering]
    ingredients = recipe["ingredients"]
    cost = recipe["cost"]

    if not order.check_resources(ingredients):
        continue

    coins = order.process_coins()
    if not order.transaction_result(coins, cost):
        continue

    order.make_sandwich(ordering, ingredients)
