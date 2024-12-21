import geometry

a = float(input("Введіть довжину сторони a: "))
b = float(input("Введіть довжину сторони b: "))
c = float(input("Введіть довжину сторони c: "))

circum_radius = geometry.circumcircle_radius(a, b, c)
print(f"Радіус описаного кола: {circum_radius:.2f}")

in_radius = geometry.incircle_radius(a, b, c)
print(f"Радіус вписаного кола: {in_radius:.2f}")
