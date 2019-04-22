#!/usr/bin/python3
# termtool.py
# Author: Nate Sales (@nwsnate)

import time

class Color:
    red = "\033[91m"
    yellow = "\033[93m"
    green = "\033[92m"
    blue = "\033[94m"
    purple = "\033[95m"

    italic = "\033[3m"
    underline = "\033[4m"
    bold = "\033[1m"

    normal = "\033[0m"

class Level:
    """ Severity presets.
    Contains a Color and icon. The reason they're separated is logfiles dont like the color codes.
    """
    SUCCESS = (Color.green + '✓' + Color.normal, "SUCCESS")  # Success, something worked.
    INFO = (Color.blue + 'ℹ️' + Color.normal, "INFO")         # Informational. Not necessarily something positive or negative. Just a heads up.
    LOW = (Color.yellow + '!' + Color.normal, "LOW")         # Small problems that won't effect the programs execution. Best practices, old versions, things to speed up performance, etc.
    MID = (Color.yellow + '✖️' + Color.normal, "MID")         # Medium priority, things that will crash the program. Dependency problems and invalid arguments would fall into this category.
    HIGH = (Color.red + '⚠️' + Color.normal, "HIGH")          # Things that effect more than just the current program. Such as the database server is down or system load is too high.
    CRITICAL = (Color.red + '☠' + Color.normal, "CRITICAL")  # The whole machine is about to go down if it hasnt already.

def event(text, level, timestamp=True, icons=True):
    """ Invoke a snaplog event. Might log to a file, might log to console.

    :param text: Message (string)
    :param level: Severity level (Level)
    :param timestamp: Include timestamp in message? (boolean)
    :param icons: Display icons instead of strings? Certian systems dont play well with certian unicode characters (boolean)

    :return Final output according to parameters: (String)
    """

    out = '['

    if icons:
        out += level[0]
    else:
        out += level[1]

    out += "] "

    if timestamp:
        out += str(time.asctime(time.localtime(time.time()))) + ' '

    out += text

    return out
