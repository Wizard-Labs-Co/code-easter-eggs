from utils.secrets import SECRET_COMMAND
from utils.egg_print import color_print
import base64
import time
import random

def _decode_hint(encoded_hint):
    try:
        return base64.b64decode(encoded_hint).decode('utf-8')
    except:
        return "Decoding failed. Keep trying."

def start():
    color_print("🐰 Welcome, developer...", "cyan")
    time.sleep(0.5)
    color_print("There are secrets hidden within the code.", "cyan")
    time.sleep(0.5)
    
    # Display a cryptic message that changes slightly each time
    cryptic_messages = [
        "The key lies not in what you see, but in what you don't.",
        "Sometimes, the answer is hidden in plain sight.",
        "Look beyond the obvious, search within the shadows.",
        "The path forward is obscured, but not invisible.",
        "What appears simple may be complex underneath."
    ]
    color_print(random.choice(cryptic_messages), "magenta")
    
    # Encoded hint that requires decoding
    encoded_hint = "b29wZW4gc2VzYW1lIGlzIHRvbyBvYnZpb3VzLCB0cnkgcmV2ZXJzaW5nIGl0"
    
    if random.random() < 0.3:  # Only show this hint sometimes
        color_print(f"Encoded hint: {encoded_hint}", "yellow")
    
    user_input = input("Type a command: ")
    
    # Make the command more complex - now it's the reverse of the secret command
    if user_input.strip().lower() == SECRET_COMMAND.lower()[::-1]:
        from game.chapter_one import begin
        begin()
    elif user_input.strip().lower() == "decode hint":
        color_print(_decode_hint(encoded_hint), "green")
        time.sleep(2)
        start()
    elif user_input.strip().lower() == SECRET_COMMAND.lower():
        color_print("That seems too obvious. Perhaps try something else?", "red")
        time.sleep(1)
        start()
    else:
        color_print("Hmm... that's not quite right.", "red")
        time.sleep(0.5)
        
        # Occasionally give a cryptic hint
        if random.random() < 0.2:
            color_print("Sometimes reversing your thinking helps...", "yellow")
        
        start()