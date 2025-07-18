def read_points(text, separator=";"):
    text = text.split(separator)
    result = []
    
    for point in text:
        x, y = point.split(",")
        new_point = {"x" : float(x), "y" : float(y)}
        result.append(new_point)
    
    return result