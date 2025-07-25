def distribute_slices(individuals):
    large_slices = individuals // 8
    medium_slices = 0
    regular_slices = (individuals % 8) // 4
    small_slices = (individuals % 8) % 4

    return large_slices, medium_slices, regular_slices, small_slices


# Example usage
individuals = 100
result = distribute_slices(individuals)
print(
    f"We need {result[0]} Large pizzas, {result[1]} Medium pizzas, {result[2]} Regular pizzas, and {result[3]} Small pizzas for {individuals} individuals.")