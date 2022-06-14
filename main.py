import os
import psutil

from base import WordsDictionary


def stop():
    process = psutil.Process(os.getpid())
    memory = process.memory_info().rss
    print(f"\nScript used \u001b[32m {memory//1024}\u001b[0m Kb of RAM.")

    exit()


def main():
    try:
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

    except KeyboardInterrupt:
        stop()


if __name__ == "__main__":
    main()
