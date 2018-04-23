# Let's look at a more advanced function that we could use to handle building a user's profile.

"""double asterisks before the parameter **user_info cause Python to create
an empty dictionary called user_info and pack whatever name-value pairs it
receives into this dictionary."""


def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile('Tommy', 'Wisseau', profession='artist', hangups='spoons')
print(user_profile)

# Using keyword arguments to potentially increase readability


def describe_alien(alien_type, alien_name):
    """Display information about an alien"""
    print("\nI have a " + alien_type + ".")
    print("My " + alien_type + "'s name is " + alien_name.title() + ".")


""" Here we'll use keyword arguments to specify what's happening when we call the function.  The function doesn't do
 anything differently, but it is more explicit what's going on. """

describe_alien(alien_type="Xenomorph", alien_name="Sue")

""" Default values can also be used in functions.  Here is a function for, perhaps, a pet adoption center.  If
we receive a pet, we'll give it a default type of dog since that's our most common animal."""


def create_pet_entry(pet_name, pet_gender, animal_type="dog"):
    """Store information about a new pet"""
    print("\nWe have received one " + pet_gender + " " + animal_type + ".")
    print("Its name is " + pet_name.title())


create_pet_entry("Willy", "Male")

# Passing Arbitrary Arguments

"""The first example in this exercise allowed us to build an arbitrarily sized dictionary using **user_info.  Let's see
the idea of arbitrary arguments one more time"""


def make_pizza(*toppings):
    """Summarize the pizza that has been requested"""
    print("\nWe are making a pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping + "")


make_pizza('pepperoni', 'olives', 'mushrooms', 'anchovies')

# Critically, the arbitrary argument must be placed last in the function def.  We may want to use a mixture of args!


def make_pizza_sized(size, *toppings):
    """Summarize the pizza and include a size"""
    print("\nWe are making a " + str(size) + "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)


make_pizza_sized(12, 'lettuce', 'fried kalamari', 'cheese curds')

