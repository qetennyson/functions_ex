def make_sandwich(*items):
    """Print a summary of the sandwich being made"""
    print("\nMaking a sandwich with the following: ")
    for item in items:
        print("- " + item)


make_sandwich('turkey', 'cheese', 'mayonnaise', 'lettuce', 'tomato', 'hot pepper')
make_sandwich('ham', 'cheese')
make_sandwich('roast beef', 'cheddar', 'onion rings', 'maple syrup')
