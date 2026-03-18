def find_max(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

a = int(input("Enter a number:\n"))
b = int(input("Enter a number:\n"))
c = int(input("Enter a number:\n"))

resultado = find_max(a, b, c)

print(f"Maximum value: {resultado}")