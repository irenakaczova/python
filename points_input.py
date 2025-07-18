user_points = input("Please enter points: ")

user_points = user_points.split(";")
result = []

for point in user_points:
    x, y = point.split(",")
    new_point = {"x" : float(x) ** 2, "y" : float(y) ** 2}
    result.append(new_point)

print(result)