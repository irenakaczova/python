from collections import namedtuple

Point = namedtuple("Points", ["x", "y"])

def read_points(text, separator=";"):
    """Reads points separated by unique separator."""

    text = text.split(separator)
    result = []
    for point in text:
        x, y = point.split(",")
        new_point = Point(float(x),float(y))
        result.append(new_point)
    
    return result