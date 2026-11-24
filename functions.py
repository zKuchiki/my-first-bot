def average(numbers):
    if not numbers:
        return None
    return sum(numbers) / len(numbers)
def top_category(totals):
    if not totals:
        return None
    best = max(totals, key=totals.get)
    return best
def count_lines(filename):
    try:
        with open(filename, encoding="utf-8") as f:
            count = 0
            for line in f:
                if line.strip():
                 count +=1
            return count
    except FileNotFoundError:
            return 0
