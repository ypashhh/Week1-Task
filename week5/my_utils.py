def average(values):
    if not values:
        return 0 # Avoid division by zero for an empty list
    return sum(values) / len(values)
