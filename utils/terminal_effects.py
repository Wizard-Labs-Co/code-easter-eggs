import os
import time
import random
from .egg_print import color_print

def matrix_rain(duration=5):
    """Creates a Matrix-style rain effect"""
    chars = "ﾊﾐﾋｰｳｼﾅﾓﾆｻﾜﾂｵﾘｱﾎﾃﾏｹﾒｴｶｷﾑﾕﾗｾﾈｽﾀﾇﾍ"
    columns = os.get_terminal_size().columns
    
    end_time = time.time() + duration
    while time.time() < end_time:
        print("\033[92m" + "".join(random.choice(chars) for _ in range(columns)))
        time.sleep(0.05)
    print("\033[0m")

def glitch_text(text, iterations=3):
    """Creates a glitch effect on text"""
    glitch_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    for _ in range(iterations):
        glitched = ''.join(c if random.random() > 0.3 else random.choice(glitch_chars) for c in text)
        color_print(glitched, "red", "fast")
        time.sleep(0.2)
    color_print(text, "green", "normal")