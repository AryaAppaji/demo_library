class InvalidValueException(Exception):
    """Raised if second parameter of the division method is zero"""

    def __init__(self):
        super().__init__("Second parameter of this method cannot be zero")