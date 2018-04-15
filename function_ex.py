def display_message():
    print("We are learning about functions in this chapter.\n")
    print("The display_message function prints two lines of text, this being the second.\n")


display_message()


def favorite_book(title):
    print("This function displays the title of a book.\n")
    print("One of my favorite books is " + title)


favorite_book("The Hobbit")


def make_shirt(size, text):
    print("You've made a " + str(size) + " shirt.\n")
    print(str(text) + "is printed on the shirt")


make_shirt("Large", "Google")
make_shirt(size="Medium", text="Nike")


def make_shirt2(size="Large", text="I love Python"):
    print("By default this function makes a " + size + " shirt, with the text " + text)


make_shirt2()


def describe_city(city, country):
    print(city + " is in " + country)


describe_city("Louisville", "USA")


def city_country(city, country):
    city_string = city + ", " + country
    return city_string


print(city_country("Louisville", "USA"))





