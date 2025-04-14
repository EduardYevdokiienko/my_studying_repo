# C = (F-32)*5/9


F = float(input("Please type your temperature in F: "))

C = (F - 32) * 5 / 9
print(f"Your temperature in C: {C:.2f}")


# def converter_temp(F=None):
#     try:
#         F = float(F)
#         C = (F - 32) * 5 / 9
#         print(f"Your temperature in C: {C:.2f}")
#     except ValueError:
#         print("Please enter a valid number.")
#
# F = input("Please type your temperature in F: ")
# converter_temp(F)