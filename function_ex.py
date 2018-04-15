def display_message():
    print("We are learning about functions in this chapter.\n")
    print("The display_message function prints two lines of text, this being the second.\n")


display_message()


def favorite_book(title):
    print("The favorite_book function displays the title of a book.")
    print("One of my favorite books is " + title + "\n")


favorite_book("The Hobbit")


def make_shirt(size, text):
    print("You've made a " + str(size) + " shirt.")
    print(str(text) + " is printed on the shirt\n")


make_shirt("Large", "Google")
make_shirt(size="Medium", text="Nike")


def make_shirt2(size="Large", text="'I Love Python'"):
    print("By default the make_shirt2 function makes a " + size + " shirt, with the text " + text + "\n")


make_shirt2()


def describe_city(city, country):
    print(city + " is in " + country + "\n")


describe_city("Louisville", "USA")


def city_country(city, country):
    city_string = city + ", " + country
    return city_string


print(city_country("Louisville", "USA"))


def make_album(name, title, tracks=''):

    album_dict = {
        'Artist': name,
        'Album': title,
        'Tracks': tracks
    }
    return album_dict


print(make_album("Kendrick Lamar", "To Pimp a Butterfly"))
print(make_album("Daft Punk", "Discovery"))
print(make_album("Fleetwood Mac", "Rumours"))
print(make_album("Bag Raiders", "Bag Raiders", 13))

# We'll define a while loop to take advantage of our make_album function, and use this to get albums from a user.

print("\nWelcome to the album storage program.  Press 'q' at any time to quit.")
while True:

    user_album = input("Please enter a music album you like: ")
    if user_album == 'q':
        break
    user_artist = input("Please enter the artist: ")
    if user_artist == 'q':
        break
    album_tracks = input("(Optional) Enter the number of tracks on the album: ")
    if album_tracks == 'q':
        break

    new_album = make_album(user_album, user_artist, album_tracks)
    print(new_album)

# We may want to pass a list into a function.
# Consider this next example where we first have a long block of code that takes a list of incomplete jobs for a 3D
# printer, prints an incomplete job, and then moves the job to a completed list.

# We will refactor this code with functions so that it is reusable, and more readable.

print("Designs that require printing\n")
unprinted_designs = ['iphone case', 'robot pendant', 'ten-sided die']
completed_models = []

print("Print simulation begins\n")
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print("Printing model: " + current_design + "...\n")
    completed_models.append(current_design)

print("List of completed models: \n")
for completed_model in completed_models:
    print(completed_model)

# With no question, this code works.  However, consider this set of code in a much larger codebase with 100s or 1000s
# of lines.  One of our goals with functions is to make each function perform as few tasks as possible, within reason.
# Then, should we realize later in our problem solving process that we need to change how that function works, we can
# easily refactor the function, rather than multiple lines of code in varying places.

# Check out how we split the operations of the above code into readable and reusable functions, with a minimum of tasks
# in each.


def print_models(unprinted_designs, completed_models):
    """
    We will use this function to simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """

    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Printing model: " + current_design)
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """Show all the models that were printed."""

    print("\n The following models were printed.")
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ['iphone case', 'android case', 'six-sided die']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

# Now are code is far more organized.  Printing models is no longer also associated with showing which models have
# been printed.  As you become a better programmer, you will see this design pattern often.  Use it, and understand it.

# The benefits (outside of arbitrary organization) are not immediately beneficial to newer programmers.  That is okay!
# You will either have to trust me, or find out for yourself after continuing to write code.  Using functions
# properly is more efficient, maintainable, and readable; it's just good practice!

# One more thing on functions and lists.  There may be times you don't want a function modifying your list.  Perhaps
# you want to keep records on the things you've printed.  You could do some strange duplication of the list inside the
# function, but the Pythonic way, and the more readable and effective way, is to simply make a copy of the list as so.

# The [:] syntax creates a copy of the list to be used by the function.  Simple as that, but only use it when necessary.
# Copying a large list might take a surprising amount of memory and time!

print_models(unprinted_designs[:], completed_models)




