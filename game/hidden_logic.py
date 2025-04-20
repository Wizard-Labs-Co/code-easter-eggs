from utils.egg_print import color_print
import random
import time
import hashlib
import sys

# This file contains hidden functionality
# It's not imported or used directly by any other file
# The user needs to discover it on their own

class _SecurityLayer:
    """A security layer that protects the hidden game"""
    def __init__(self):
        self._key = hashlib.sha256(str(random.randint(1, 1000)).encode()).hexdigest()[:8]
        self._authorized = False
    
    def authorize(self, key=None):
        """Authorizes access to the hidden game"""
        if key == self._key:
            self._authorized = True
            return True
        return False
    
    def is_authorized(self):
        """Checks if access is authorized"""
        return self._authorized
    
    def get_key_hint(self):
        """Returns a hint about the key"""
        return f"Key starts with: {self._key[:2]}..."

_security = _SecurityLayer()

def _hidden_game():
    """
    A complex number guessing mini-game
    This is a hidden feature!
    """
    if not _security.is_authorized():
        color_print("Access denied. Security authorization required.", "red")
        color_print(f"Security hint: {_security.get_key_hint()}", "yellow")
        color_print("Try calling _security.authorize() with the correct key.", "yellow")
        return False
    
    color_print("🎮 You've discovered a hidden mini-game!", "cyan")
    color_print("This is a complex number guessing game with a twist.", "cyan")
    time.sleep(1)
    
    # Generate a sequence instead of a single number
    sequence_length = random.randint(3, 5)
    sequence = [random.randint(1, 10) for _ in range(sequence_length)]
    
    color_print(f"I'm thinking of a sequence of {sequence_length} numbers between 1 and 10.", "cyan")
    color_print("You need to guess each number in the sequence.", "cyan")
    
    correct_guesses = 0
    for i in range(sequence_length):
        tries_left = 3
        while tries_left > 0:
            try:
                guess = int(input(f"Position {i+1} ({tries_left} attempts left): "))
                if guess == sequence[i]:
                    color_print("Correct!", "green")
                    correct_guesses += 1
                    break
                elif guess < sequence[i]:
                    color_print("Too low!", "yellow")
                else:
                    color_print("Too high!", "yellow")
                tries_left -= 1
            except ValueError:
                color_print("Please enter a valid number!", "red")
                tries_left -= 1
        
        if tries_left == 0:
            color_print(f"The number at position {i+1} was {sequence[i]}.", "magenta")
    
    if correct_guesses == sequence_length:
        color_print("🎉 You got the entire sequence! You're truly a code explorer!", "green")
        color_print("You've earned the right to access the ultimate secret.", "green")
        color_print("Try calling the ultimate_secret() function.", "yellow")
        return True
    else:
        color_print(f"You got {correct_guesses} out of {sequence_length} correct.", "magenta")
        color_print("Better luck next time!", "magenta")
        return False

# This function is the ultimate easter egg, but it's protected
def ultimate_secret():
    """The final secret - congratulations if you found this!"""
    # Check if the function was called directly by the user
    frame = sys._getframe(1)
    caller_module = frame.f_globals.get('__name__', '')
    
    if caller_module != '__main__' and not _security.is_authorized():
        color_print("Access to the ultimate secret is restricted.", "red")
        color_print("You must prove your worth by completing the hidden game first.", "yellow")
        color_print("Try calling _hidden_game() first.", "yellow")
        return
    
    color_print("🏆 CONGRATULATIONS! 🏆", "green")
    time.sleep(1)
    color_print("You've discovered the ultimate secret function!", "green")
    time.sleep(1)
    color_print("You are truly a master code explorer.", "cyan")
    time.sleep(1)
    
    # ASCII art celebration with a twist - it's encoded
    encoded_celebration = """
    KiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAqCiogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgKgogKiAgICAgICAgICAgICAgICAgICAgICBZT1UgRElEIElUISAgICAgICAgICAgICAgICAgICAgICAgKgogICogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICogIAogICAqICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgKiAgIAogICAgKiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAqICAgIAogICAgICogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICogICAgIAogICAgICAgKiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgKiAgICAgIAogICAgICAgICAqICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAqICAgICAgICAKICAgICAgICAgICAqICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAqICAgICAgICAgIAogICAgICAgICAgICAgKiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgKiAgICAgICAgICAgIAogICAgICAgICAgICAgICAqICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAqICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAqICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAqICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgKiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgKiAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAqICAgICAgICAgICAgICAgICAgICAgICAgICAqICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAqICAgICAgICAgICAgICAgICAgICAgICAqICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgKiAgICAgICAgICAgICAgICAgICAqICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICogICAgICAgICAgICAgICAqICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAqICAgICAgICAgICAqICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgKiAgICAgICAqICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICogICAgKiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgKiAqICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAo=
    """
    
    # Let the user decode it themselves
    color_print("I have one last challenge for you...", "cyan")
    color_print("Decode this message to see your final reward:", "cyan")
    color_print(encoded_celebration, "yellow")
    color_print("Hint: It's base64 encoded.", "magenta")