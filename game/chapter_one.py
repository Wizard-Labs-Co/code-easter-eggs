from utils.egg_print import color_print
import time
import random
import hashlib

def _generate_puzzle():
    """Generates a simple math puzzle with a twist"""
    operations = ['+', '-', '*']
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    op = random.choice(operations)
    
    if op == '+':
        result = a + b
    elif op == '-':
        result = a - b
    else:
        result = a * b
    
    return f"{a} {op} {b}", result

def _check_answer(puzzle_hash, user_answer):
    """Checks if the user's answer matches the expected hash"""
    try:
        user_answer = int(user_answer.strip())
        answer_hash = hashlib.md5(str(user_answer).encode()).hexdigest()[:10]
        return answer_hash == puzzle_hash
    except:
        return False

def begin():
    color_print("🥚 You found something...", "green")
    time.sleep(1)
    color_print("But the path forward is locked behind a puzzle.", "green")
    time.sleep(1)
    
    # Generate a puzzle
    puzzle, answer = _generate_puzzle()
    # Create a hash of the answer
    answer_hash = hashlib.md5(str(answer).encode()).hexdigest()[:10]
    
    color_print(f"Solve this: {puzzle}", "yellow")
    color_print(f"The answer hash should match: {answer_hash}", "yellow")
    color_print("(Hint: The answer is a number)", "cyan")
    
    user_input = input("Your answer: ")
    
    if _check_answer(answer_hash, user_input):
        color_print("Correct! You may proceed.", "green")
        time.sleep(1)
        color_print("There's a module named ascii_egg that might interest you...", "yellow")
        time.sleep(0.5)
        color_print("But how to use it? That's for you to discover.", "yellow")
        
        # Add a cryptic hint about the next step
        if random.random() < 0.3:
            color_print("Sometimes you need to import knowledge before revealing it.", "magenta")
    else:
        color_print("That's not right. Try again.", "red")
        time.sleep(1)
        begin()  # Restart the puzzle with a new one

# Hidden function that's not referenced directly
def _secret_passage():
    """A hidden function that provides a hint to the next step"""
    color_print("You've found a secret passage!", "green")
    color_print("To reveal the egg, you must import the module and call its function.", "cyan")
    color_print("Try: from game.ascii_egg import reveal", "yellow")
    color_print("Then: reveal()", "yellow")
    
    # This is a very hidden hint about the chocolate
    if random.random() < 0.1:  # Only 10% chance to see this
        color_print("There's also something about chocolate hidden in the same file...", "magenta")