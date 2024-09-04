class UsernameAlreadyTaken(Exception):
    def __init__(self, username: str = ""):
        self.message = f"""
        Username {username} is already taken.
        """


class EmailAlreadyTaken(Exception):
    def __init__(self, email: str = ""):
        self.message = f"""
        Email {email} is already taken.
        """

# Below code is the same as the above.


# class UsernameAlreadyTaken(Exception):
#     def __init__(self, username: str = ""):
#         message = f"Username '{username}' is already taken."
#         super().__init__(message)

# class EmailAlreadyTaken(Exception):
#     def __init__(self, email: str = ""):
#         message = f"Email '{email}' is already taken."
#         super().__init__(message)