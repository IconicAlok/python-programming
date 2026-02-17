# Formatt specifiers = {: flags} formatt a value vased on what
#                               flag are inserted

# :.(number)f = round to that many decemal places (fixed point)
# :(number) = allocate that many spaces
# :03 = alocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indecate positive value
# := = place sign to left most position
# : = insert a space before positive numbers
# :, = comma separator



price1 = 3000.14159
price2 = -9870.65
price3 = 1200.34

print(f"price1 ${price1:+,.2f} ")
print(f"price2 ${price2:+,.2f}")
print(f"price1 ${price3:+,.2f}")