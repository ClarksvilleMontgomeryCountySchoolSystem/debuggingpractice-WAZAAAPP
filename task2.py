# Debugging Challenge - Part 2: Input and Data Conversion Errors

# --- Predefined Test Values (used when main() is commented out) ---
candy_quantity_str = "3"
soda_quantity_str = "2"
gallons_str = "10.5"
pounds_str = "1.25"
lottery_quantity_str = "5"


def main():
    global candy_quantity_str, soda_quantity_str, gallons_str, pounds_str, lottery_quantity_str
    candy_quantity_str = input("How many candy bars? ")
    soda_quantity_str = input("How many sodas? ")
    gallons_str = input("How many gallons of gas? ")
    pounds_str = input("How many pounds of deli meat? ")
    lottery_quantity_str = input("How many lottery tickets? ")


# Comment out the line below after fixing input bugs
main()


# --- Receipt Header ---
print("""
========================================
       GAS STATION RECEIPT
      Thank you for shopping!
========================================
""")

# --- Candy Bars ---
candy_price = 1.89
candy_quantity = int(candy_quantity_str)
candy_total = candy_price * candy_quantity
print(f"Candy Bars: {candy_quantity} x ${candy_price} = ${candy_total:.2f}")

# --- Soda Bottles ---
soda_price = 2.49
soda_quantity = int(soda_quantity_str)
soda_total = soda_price * soda_quantity
print(f"Soda: {soda_quantity} x ${soda_price} = ${soda_total:.2f}")

# --- Gas ---
gas_price = 3.25
gallons = float(gallons_str)
gas_total = gas_price * gallons
print(f"Gas: {gallons} gallons x ${gas_price} = ${gas_total:.2f}")

# --- Deli Meat ---
deli_price = 8.99
pounds = float(pounds_str)
deli_total = deli_price * pounds
print(f"Deli Meat: {pounds} lbs x ${deli_price} = ${deli_total:.2f}")

# --- Lottery Tickets ---
lottery_price = 2
lottery_quantity = int(lottery_quantity_str)
lottery_total = lottery_price * lottery_quantity
print(f"Lottery: {lottery_quantity} x ${lottery_price} = ${lottery_total:.2f}")

# --- Receipt Total ---
receipt_total = candy_total + soda_total + gas_total + deli_total + lottery_total

print(f"""
========================================
TOTAL: ${receipt_total:.2f}
========================================
Thank you! Come again!
""")