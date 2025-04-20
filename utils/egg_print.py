import time
import random
import sys

def color_print(text, color="white", speed="normal", special_effect=None):
    """
    Prints colored text to the terminal with various effects
    
    Colors available:
    - black
    - red
    - green
    - yellow
    - blue
    - magenta
    - cyan
    - white
    
    Speeds:
    - fast
    - normal
    - slow
    
    Special effects:
    - blink
    - bold
    - underline
    - reverse
    """
    colors = {
        "black": "\033[30m",
        "red": "\033[31m",
        "green": "\033[32m",
        "yellow": "\033[33m",
        "blue": "\033[34m",
        "magenta": "\033[35m",
        "cyan": "\033[36m",
        "white": "\033[37m",
        "reset": "\033[0m"
    }
    
    effects = {
        "blink": "\033[5m",
        "bold": "\033[1m",
        "underline": "\033[4m",
        "reverse": "\033[7m"
    }
    
    speeds = {
        "fast": 0.01,
        "normal": 0.03,
        "slow": 0.1
    }
    
    # Apply color and effect
    output = colors.get(color, colors["white"])
    if special_effect and special_effect in effects:
        output += effects[special_effect]
    
    # Get the speed
    delay = speeds.get(speed, speeds["normal"])
    
    # Print character by character for a typing effect
    for char in text:
        sys.stdout.write(output + char + colors["reset"])
        sys.stdout.flush()
        time.sleep(delay * (0.5 + random.random()))
    
    print()  # New line at the end

# Hidden function that can create ASCII art animations
def _animate_ascii(ascii_art, color="cyan", frames=3, delay=0.2):
    """Creates a simple animation with ASCII art"""
    for _ in range(frames):
        # Clear the terminal (works on most terminals)
        print("\033c", end="")
        
        # Print the ASCII art
        color_print(ascii_art, color)
        
        # Wait
        time.sleep(delay)
        
        # Clear again
        print("\033c", end="")
        
        # Print a slightly modified version
        modified = ascii_art.replace("(", "{").replace(")", "}").replace("<", "[").replace(">", "]")
        color_print(modified, "magenta")
        
        # Wait
        time.sleep(delay)