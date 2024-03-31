

# noinspection PyUnusedLocal
# friend_name = unicode string
def hello(friend_name: str) -> str:
    if not isinstance(friend_name, str):
        raise ValueError("friend_name should by a type of string!")
    return "Hello, World!"
