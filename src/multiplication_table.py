
def multiplication_table(n: int, limit: int ) -> list:
    if not isinstance(n, int) or not isinstance(limit, int):
        raise TypeError("n and limit must be positive integers!")
    if limit <= 0:
        raise ValueError("Limit must be a positiv number!")
    result = []
    for item in range(1, limit + 1):
        result.append(n * item)
    return result