import time

def counter(validated_input):
    for x in reversed(range(0, validated_input + 1)):
        print(x)
        time.sleep(1)


