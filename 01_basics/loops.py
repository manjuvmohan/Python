"""
Demonstrates loops in Python
- for loop
- while loop
"""
def count_with_for(n : int) :
    for i in range(1,n+1):
        print("for loop",i)
def count_with_while(n : int):
    i=1
    while(i<=n) :
        print("while loop ", i)
        i=i+1

if __name__ == "__main__" :
    count_with_for(3)
    count_with_while(3)