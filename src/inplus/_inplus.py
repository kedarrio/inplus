class Input:
    """
    Holds Methods for asking inputs from users.
    """
    @classmethod
    def string(cls, prompt: str = None) -> str:
        """string
        ask a input from user and return a string.
        (same as input())

        Args:
            prompt (str, optional): prompt message. Defaults to None.

        Returns:
            str: input string.
        """
        if not prompt: prompt = "enter"
        return input(f'> {prompt} : ')
