def print_rhombus(width, height):
    for i in range(height // 2):
        spaces = ' ' * (width // 2 - i)
        stars = '*' * (2 * i + 1)
        print(spaces + stars)
    for i in range(height // 2, -1, -1):
        spaces = ' ' * (width // 2 - i)
        stars = '*' * (2 * i + 1)
        print(spaces + stars)

width = int(input("Введіть ширину ромба: "))
height = int(input("Введіть висоту ромба: "))

print_rhombus(width, height)
