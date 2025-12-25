class DepthValueIsNotValidException(Exception):
    def __init__(
        self,
        message="Recursion depth is not valid. Please, enter any digit between 1 and 1000.",
    ):
        super().__init__(message)
