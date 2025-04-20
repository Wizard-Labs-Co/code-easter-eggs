import random
import hashlib

class PuzzleGenerator:
    def __init__(self, difficulty=1):
        self.difficulty = difficulty
        self.operators = ['+', '-', '*']
    
    def generate_puzzle(self):
        """Generates a math puzzle based on difficulty"""
        if self.difficulty == 1:
            a = random.randint(1, 10)
            b = random.randint(1, 10)
            op = random.choice(self.operators)
            puzzle = f"{a} {op} {b}"
        else:
            nums = [random.randint(1, 20) for _ in range(self.difficulty + 1)]
            ops = [random.choice(self.operators) for _ in range(self.difficulty)]
            puzzle = str(nums[0])
            for i in range(self.difficulty):
                puzzle += f" {ops[i]} {nums[i+1]}"
        
        result = eval(puzzle)  # Calculate the result
        result_hash = hashlib.md5(str(result).encode()).hexdigest()[:8]
        
        return puzzle, result, result_hash
    
    def verify_answer(self, answer, result_hash):
        """Verifies if the answer matches the hash"""
        try:
            answer = int(answer)
            answer_hash = hashlib.md5(str(answer).encode()).hexdigest()[:8]
            return answer_hash == result_hash
        except:
            return False