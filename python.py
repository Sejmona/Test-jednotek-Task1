class IntegerSet:
    def __init__(self, numbers):
        if not all(isinstance(num, int) for num in numbers):
            raise ValueError("All elements must be integers")
        self.numbers = set(numbers)
    
    def sum(self):
        return sum(self.numbers)
    
    def average(self):
        return sum(self.numbers) / len(self.numbers) if self.numbers else 0
    
    def maximum(self):
        return max(self.numbers) if self.numbers else None
    
    def minimum(self):
        return min(self.numbers) if self.numbers else None
