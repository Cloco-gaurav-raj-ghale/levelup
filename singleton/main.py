# we will be working with only one instance

from singleton.example.logger import Logger
def main():
    s1 = Logger.get_instance()
    s2 = Logger.get_instance()
    # since we already checked for instance in get_instance. we will get same instance in s1 and s2.
    if s1 is s2:
        print("Logger is a singleton")

    s1.log("Logging with logger1")
    s2.log("Logging with logger2")

    print(s1, s2)

if __name__ == "__main__":
    main()