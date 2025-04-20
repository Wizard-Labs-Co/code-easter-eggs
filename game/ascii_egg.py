import os
from utils.egg_print import color_print
import time
import random
import inspect

class _EggProtection:
    """A class that protects the egg reveal functionality"""
    def __init__(self):
        self._access_code = random.randint(1000, 9999)
        self._attempts = 0
        self._max_attempts = 3
        self._locked = False
    
    def check_access(self, code=None):
        """Checks if access is granted to reveal the egg"""
        # If called from reveal(), grant access
        caller = inspect.currentframe().f_back.f_code.co_name
        if caller == 'reveal':
            return True
            
        # Otherwise require the access code
        if self._locked:
            color_print("Access is locked. Try again later.", "red")
            return False
            
        if code is None:
            color_print(f"Access code required. Hint: {self._access_code // 100}XX", "yellow")
            return False
            
        self._attempts += 1
        if code == self._access_code:
            color_print("Access granted!", "green")
            return True
        else:
            remaining = self._max_attempts - self._attempts
            if remaining > 0:
                color_print(f"Access denied. {remaining} attempts remaining.", "red")
            else:
                color_print("Too many failed attempts. Access locked.", "red")
                self._locked = True
            return False

_protection = _EggProtection()

def reveal():
    """
    Reveals a hidden ASCII art bunny.
    This function is not called automatically.
    It's meant to be discovered by curious developers.
    """
    if not _protection.check_access():
        return
        
    try:
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        with open(os.path.join(base_dir, "assets/ascii/bunny.txt"), "r") as f:
            bunny_art = f.read()
            
            # Add some animation
            for line in bunny_art.split('\n'):
                color_print(line, "magenta")
                time.sleep(0.1)
                
            color_print("You found the bunny! But there's more to discover...", "green")
            
            # Cryptic hint about the chocolate
            color_print("The bunny guards something sweet...", "yellow")
            color_print("Look deeper into this module's source code.", "yellow")
            
            # Very subtle hint about hidden_logic.py
            if random.random() < 0.3:
                color_print("Logic is sometimes hidden in plain sight.", "cyan")
    except Exception as e:
        color_print(f"Oops! Something went wrong: {e}", "red")

# This function is obfuscated to make it harder to find
def __getattr__(name):
    if name == '_' + 's' + 'ecret' + '_' + 'cho' + 'colate':
        def _hidden_func():
            try:
                base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
                with open(os.path.join(base_dir, "assets/ascii/chocolate_egg.txt"), "r") as f:
                    egg_art = f.read()
                    color_print(egg_art, "yellow")
                    color_print("🍫 Sweet! You found the chocolate egg!", "green")
                    color_print("But the ultimate secret remains hidden...", "green")
                    
                    # Hint about hidden_logic.py
                    color_print("Sometimes logic is hidden where you least expect it.", "magenta")
            except Exception as e:
                color_print(f"Oops! Something went wrong: {e}", "red")
        return _hidden_func
    raise AttributeError(f"module 'ascii_egg' has no attribute '{name}'")

# The actual _secret_chocolate function is hidden and can only be accessed indirectly
def _secret_chocolate():
    """This is a decoy function"""
    color_print("Nice try, but the real chocolate is hidden elsewhere...", "red")
    color_print("Look deeper into how Python modules work.", "yellow")