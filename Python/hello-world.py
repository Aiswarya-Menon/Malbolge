import time

message = "Hello, World!"
for char in message:
    print(char, end='', flush=True)
    time.sleep(0.5)
