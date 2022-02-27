def find_y_intercept(x_coordinate, y_coordinate):
    m = int(input("In put your slope(m): "))
    x = x_coordinate
    y = y_coordinate
    if type(m) == int:
        print(y / (m * x))
    else:
        print("Input data type is incorrect! Please enter a number")