def circle(radius):
    """Calculate area of circle.
    """
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return 3.14159 * radius * radius