class Logger:
    _instance = None

    def __init__(self):
        """
            Pythonic way of creating singleton
        """
        raise RuntimeError("Call get_instance() instead")

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def log(self, message):
        print(f"Log: {message}")