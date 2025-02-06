def convert_to_coins(dollars):
    cents = int(dollars * 100)

    quarters = 0
    dimes = 0
    nickels = 0
    pennies = 0

    quarters = cents // 25
    cents %= 25

    dimes = cents // 10
    cents %= 10

    nickels = cents // 5
    cents %= 5

    pennies = cents

    return quarters, dimes, nickels, pennies


dollars = float(input("Enter Dollar Ammount"))
quarters, dimes, nickels, pennies = convert_to_coins(dollars)
print(f"For ${dollars:.2f}, you can make {quarters} quarters, {dimes} dimes, {nickels} nickels, and {pennies} pennies.")
