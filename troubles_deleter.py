## "Cool" character input
## getch() allows keypresses without displaying them

# thank you https://gist.github.com/jfktrey/8928865
import platform

if platform.system() == "Windows":
    import msvcrt
    def getch():
        return msvcrt.getch()
else:
    import tty, termios, sys
    def getch():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

## helper function: cool overwrite function
import random
import time
symbols = ("*", "+", "#", "°", "×", '⋅')
def overwrite(n):
    finals = ''
    # choose how many "animated" symbols to draw over each letter
    plan = [random.randint(3,10) for i in range(n)]
    for i in plan:
        for i in range(i):
            symbol = random.choice(symbols)
            # reprint complete line up to the current spot
            print('\r' + finals + symbol, end='', flush=True)
            time.sleep(0.05)
        finals += symbol
    print('\r' + '!' * n) 

## Activity code

print("What's troubling you?")
last = None
txt = ''
while True:
    last = getch()
    if last != '\r':
        txt += last
        print(last, end='', flush=True)
    else:
        break

print('\r', end='') # carriage return - move cursor to start of line
overwrite(len(txt))
print(f"Glad that it's off your chest! I know you'll get through it.\nYou don't have to worry about {repr(txt)} anymore.")
