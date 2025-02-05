
def find_median(numbers: list) -> float:
    if not numbers:
        return None

    numbers.sort()
    n = len(numbers)
    mid = n // 2

    if n % 2 == 1:
        return numbers[mid]
    else:
        return (numbers[mid - 1] + numbers[mid]) / 2


