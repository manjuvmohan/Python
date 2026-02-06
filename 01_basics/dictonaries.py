"""
Demonstrates dictionary usage in Python
- key-value pairs
- iteration
- common dictionary operations
"""

def process_dict(cities: dict[str:str]) -> None:
    #looping through the dictionary
    for i in cities :
        print("cities only __",cities[i])

    for x,y in cities.items() :
        print("countries and cities" ,x,y)

    for x in cities.keys():
        print("by keys",x,cities[x])

    #access an item from dictionary
    print("Famous city in India ",cities["India"])
    print("Famous city in India ",cities.get("India"))

    #checking if a vlaue exists in the dictioanry
    if "India" in cities :
        print("Yes, India is in the dictionary")

    # get the keys from dictionary
    print("Keys in ths dictionary are",cities.keys())

    # get the values from dictionary
    print("values in ths dictionary are",cities.values())

    #adding an item to dictionary
    cities["Canada"] = "Toronto"
    print(cities)
    #deleting an item from dictionary
    cities.pop("India")
    print(cities)

    #deleting the last item inserted from dictionary
    cities.popitem()
    print(cities)
    #updating an item in dictionary
    cities["USA"] = "SFO"
    print(cities)

    #emptying the dictionary
    cities.clear()
    print(cities)

if __name__ == "__main__" :
    cities = {"USA" : "New York",
            "Japan" : "Tokyo",
            "India" : "Mumbai"

    }

    process_dict(cities)