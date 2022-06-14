from base import WordsDictionary


def main():

    while True:
        user_input = input("Enter num (Add, Random show or Guess words): ")

        match user_input:
            case "1":
                WordsDictionary.add()
            case "2":
                WordsDictionary.show()
            case "3":
                WordsDictionary.guess()
            case "config":
                WordsDictionary.config()

        print("Unsupported input, try again.")


if __name__ == "__main__":
    main()
