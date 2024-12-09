from typing import Optional


class InputError(Exception):
    def __init__(self, input_name, message: Optional[str] = None):
        if message is None:
            message = f"Invalid input: {input_name}."
        self.message = f"Invalid input: {input_name}. {message}"
        super().__init__(self.message)
