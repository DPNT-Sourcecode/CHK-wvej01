# noinspection PyShadowingBuiltins,PyUnusedLocal
def compute(x: int, y: int) -> int:
    for number in [x, y]:
        if not 0 <= number <= 100:
            raise ValueError("Values should be a positive integer between 0-100")
    return x + y

