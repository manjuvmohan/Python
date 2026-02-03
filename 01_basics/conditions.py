"""
Demonstrates conditional statements in Python
- if
- elif
- else
"""
def check(number :int) -> str :
    if number > 0 :
        return "positve"
    elif number < 0 :
        return "negative"
    else :
        return "zerio"
if __name__ == "__main__":
    numbers = [10,0,-1]
    for n in numbers :
        print(f"{n} is {check(n)}")

