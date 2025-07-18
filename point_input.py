user_point = input("Please enter a point where x and y coordinates are separated by comma (i.e. 20,-10.23): ")

comma_index = user_point.index(",")
x = float(user_point[0:comma_index])
y = float(user_point[comma_index+1:])

print("x^2: {}, y^2: {}".format(x ** 2, y ** 2))