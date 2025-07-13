class Car:
    # constructor method (yung def __init__) para mag-set ng values kapag gumawa tayo ng Car object
    def __init__(self, make, model, year):
        self.make = make      # Brand ng car (e.g., Tesla, Porsche)
        self.model = model    # Model ng car (e.g., Model S, 911)
        self.year = year      # Year ng car (e.g., 2023)

    # method to describe the car
    def describe(self):
        # gagawa ng string na nagsasabi kung anong car ito
        return f"This car is a {self.year} {self.make} {self.model}."

# Printing

car1 = Car("Porsche", "911 Turbo S", 2022)
print(car1.describe())  # Output: This car is a 2022 Porsche 911 Turbo S.

car2 = Car("Tesla", "Model S Plaid", 2023)
print(car2.describe())  # Output: This car is a 2023 Tesla Model S Plaid.

car3 = Car("Lamborghini", "Huracán EVO", 2021)
print(car3.describe())  # Output: This car is a 2021 Lamborghini Huracán EVO.
