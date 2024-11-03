from singleton.example.logger import Logger


def main():
    s1 = Logger.get_instance()
    s2 = Logger.get_instance()
    if s1 is s2:
        print("Logger is a singleton")

    s1.log("Logging with logger1")
    s2.log("Logging with logger2")

    print(s1, s2)

if __name__ == "__main__":
    main()