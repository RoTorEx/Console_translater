import os
import psutil

from base import WordsDictionary


def stop():
    process = psutil.Process(os.getpid())
    memory = process.memory_info().rss

    print(f"\nThe script has been stopped. It used \u001b[32m {memory//1024}\u001b[0m Kb of RAM.")
    exit()


def main():
    # class_methods = filter(lambda meth: not meth.startswith("__"), dir(WordsDictionary))

    try:
        while True:
            user_input = input("Enter preferred work type: ").lower().strip()

            try:
                eval(f"WordsDictionary.{user_input}()")
                stop()

            except AttributeError:
                print("Unsupported method. Сheck out the documentation and try again.")
                continue

    except KeyboardInterrupt:
        stop()


if __name__ == "__main__":
    main()
