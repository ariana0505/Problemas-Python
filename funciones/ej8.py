import math

def _find_mean(numbers : list):
    return sum(numbers)/len(numbers) if numbers else 0

def _find_variance(numbers: list):
    mean = _find_mean(numbers)
    squared_diffs = [(x - mean) ** 2 for x in numbers]  
    return sum(squared_diffs) / len(numbers)
def _find_standard_deviation(variance):
    return math.sqrt(variance)
