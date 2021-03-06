def get_string_from_user(msg):
    inp = str(input(msg))
    return inp

while True:
    try:
        user_name = get_string_from_user("Enter your name, please: ")
        user_place = get_string_from_user("Where are you from?: ")
        print("Hello {}! How is the weather in {} today?".format(user_name, user_place))
    except EOFError:
        print("***Oops, something went wrong! Try again!")
    except KeyboardInterrupt:
        print("***Oops, something went wrong! Try again!")
    except BaseException:
        print("***Oops, something went wrong! Try again!")
    else:
        break
        