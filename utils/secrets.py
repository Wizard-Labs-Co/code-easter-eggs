# This file contains encoded values
# Decoding them is part of the challenge

import base64

def _decode(s):
    return base64.b64decode(s).decode('utf-8')

# The actual secrets are encoded
_ENCODED_SECRET_COMMAND = "b3BlbiBzZXNhbWU="  # "open sesame" encoded
_ENCODED_EASTER_EGG_TRIGGER = "ZWdnLnJldmVhbCgp"
_ENCODED_CHOCOLATE_EGG_COMMAND = "X3NlY3JldF9jaG9jb2xhdGUoKQ=="
_ENCODED_ULTIMATE_SECRET_FUNCTION = "dWx0aW1hdGVfc2VjcmV0KCk="

# These are decoy variables to confuse the player
RED_HERRING_1 = "this_is_not_the_command_you_seek"
RED_HERRING_2 = "try_harder"
RED_HERRING_3 = "almost_there_but_not_quite"

# The actual values are hidden behind a function call
SECRET_COMMAND = _decode(_ENCODED_SECRET_COMMAND)
EASTER_EGG_TRIGGER = _decode(_ENCODED_EASTER_EGG_TRIGGER)
CHOCOLATE_EGG_COMMAND = _decode(_ENCODED_CHOCOLATE_EGG_COMMAND)
ULTIMATE_SECRET_FUNCTION = _decode(_ENCODED_ULTIMATE_SECRET_FUNCTION)

# Cryptic hint system
def get_hint(level):
    hints = {
        1: "Look at the source, not the output",
        2: "Functions can hide other functions",
        3: "Sometimes what you seek is backwards",
        4: "The chocolate is hidden where the bunny can't reach",
        5: "Ultimate secrets require ultimate patience"
    }
    return hints.get(level, "No hint available for that level")

# Hidden message in the comments:
# If you're reading this, you're on the right track.
# But remember, the key is not what it seems.
# Try: emases nepo