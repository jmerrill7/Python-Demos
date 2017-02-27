#PURPOSE python course drill, demonstrating how to pass variables from
#functon to function


def start():
    print("Hello {}".format(get_name()))

def get_name():
    name = raw_input("what's your name? ")
    return name











if __name__ == "__main__":
    start()
