def make_sandwich(*items):
    """Print a summary of the sandwich being made"""
    print("\nMaking a sandwich with the following: ")
    for item in items:
        print("- " + item)


make_sandwich('turkey', 'cheese', 'mayonnaise', 'lettuce', 'tomato', 'hot pepper')
make_sandwich('ham', 'cheese')
make_sandwich('roast beef', 'cheddar', 'onion rings', 'maple syrup')


def store_car_info(manuf, model, **car_info):
    """Note: PyCharm catches this and calls for building a dict literal as seen.  This is slightly faster than
    assignment as in the adv_functions.py profile example.  Jury is out on value."""
    car_data = {
       'Manufacturer': manuf,
       'Model': model,
    }
    for key, value in car_info.items():
        car_data[key] = value

    return car_data


honda = store_car_info('Honda', 'Civic', engine='Turbo I4', trans='auto', body='coupe')

print(honda)
