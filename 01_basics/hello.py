"""
Basic hello code
print the name
add two integers
"""
def add(a:int, b:int) -> int:
    return a+b
def greet(name : str) -> str :
    return f'Hello {name}'
if __name__ == "__main__":
    print(greet("Manju"))
    print("2+3=",add(2,3))