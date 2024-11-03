class Logger:
    _instance = None

    def __init__(self):
        """
            creation of new object is prohibited
        """
        raise RuntimeError("Call get_instance() instead")

    @classmethod
    def get_instance(cls):
        # checking is we have an instance of this class and if not creating new.
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def log(self, message):
        print(f"Log: {message}")