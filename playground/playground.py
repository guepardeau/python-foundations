# rows = int(input ("Enter the number of rows:"))
# columns = int(input ("Enter the number of columns:"))
# symbol = input ("Enter the symbol: ")



# for x in range(rows):    
#     for y in range (columns):
#         print (symbol, end="")
#     print()   
# # NESTED LOOPS


# COLLECTIONS - SINGLE 'VARIABLE USED TO STORE MULTIPLE VALUES
    # LIST = [] ORDERED AND CHANGEABLE. DUPLICATES OK
    # SET = {} UNORDERED (prints randomly) AND IMMUTABLE, BUT ADD/REMOVE OK. NO DUPLICATES
    # TUPLE = () ORDERED AND UNCHANGEABLE. DUPLICATES OK. FASTER, USE OVER LISTS WHEN POSSIBLE.

        # fruits = ["Apple", "Oranges", "Banana", "Coconut"]
        # print(dir(fruits))
        # print(help(fruits))
        # print(len(fruits))

        # fruits.append("Pineapple")
        # fruits.remove("Apple")
        # fruits.insert(0, "pineapple")
        # fruits.sort()
        # fruits.reverse()
        # fruits.clear()
        # print(fruits.index("Apple"))
        # print(fruits.count("Banana"))
        # print(fruits)

        # # LISTS + some Methods.

        # fruits = {"Apple", "Oranges", "Banana", "Coconut"}
        # fruits.add("pineapple")
        # fruits.remove("Apple")
        # fruits.pop()
        # fruits.clear()
        # print(fruits)
        # # print("pineapple" in fruits)
        # # NO INDEXING ON SETS I.E NO [0] RANDOM ORDER, IMMUTABLE, works well with constants - i.e colours.

        # fruits = ("apple", "orange", "banana", "coconut", "coconut")
        # print(fruits.index("coconut"))
        # print(fruits.count("coconut"))

        # for fruit in fruits:
        #     print(fruit)