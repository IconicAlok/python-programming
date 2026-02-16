# logial operator = Evaluate multiple conditions (and, or, not)
#                     or = at least one condition to be True
#                     and = both condition must be True
#                     not = inverts the condition (not false not true)




# temp = 20
# is_rainning = True
#
# if temp > 35 or temp < 0 or is_rainning:
#     print("The outdor event is cancelled")
# else:
#     print("The outdor event is still scheduled")


temp = 20
is_sunny = False
if temp >= 28 and is_sunny:
    print("It is HOT outside")
    print("It is sunny")
elif temp <= 0 and is_sunny:
    print("It is COLD outside")
    print("It is sunny")
elif 28 > temp > 0 and is_sunny:
    print("It is warm outside")
    print("It is sunny")
elif temp >= 28 and not is_sunny:
    print("It is HOT outside")
    print("It is CLOUDY")
elif temp <= 0 and not is_sunny:
    print("It is COLD outside")
    print("It is CLOUDY")
elif 28 > temp > 0 and not is_sunny:
    print("It is warm outside")
    print("It is CLOUDY")

