"""
Demonstrates list operations
- creating lists
- iterating over lists
- basic list functions
"""

def process_fruits(fruits : list[str]) -> None :
    for fruit in fruits :
        print("the fruit list is ",fruit)
    
    

if __name__ == "__main__" :
    fruits = ["mango","orange","apple"]
    process_fruits(fruits) 

    print("length of the first fruit list is", len(fruits))

    fruits_new = ["kiwi","apple","pear"]
    process_fruits(fruits_new)
    print("length of the second fruit list is ",len(fruits_new))
    fruits_combined = fruits + fruits_new
    print("combining two lists" , fruits_combined)
    fruits.append("pineapple")
    print("List append -- after sppending fruits",fruits)
    fruits.remove("mango")
    print("List removal -- after removing fruits", fruits)
    print("# of apples in the list",fruits_combined.count("apple"))
    fruits.reverse()
    print(f"list reversed {fruits}")
    print("index of apple in the list is ",fruits.index("apple"))
    print("index ------fruit at index 2 is ",fruits[2])
    fruits.sort()
    print("sorting the list---default ",fruits)
    fruits.sort(reverse="true")
    print("sorting the list---descending ",fruits)
    fruits_new.sort(key=len)
    print("sorting the list---based on length ",fruits_new)
    fruits.insert(1,"banana")
    print("after inserting banana at index 1 --- ", fruits)
    