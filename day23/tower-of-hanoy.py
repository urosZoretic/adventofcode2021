def TowerOfHanoi(n, source, destination, auxiliary):
    if n == 1:
        print ("ho Move disk 1 from source", source, "to destination", destination)
        return
    print("to one: ", source, destination, auxiliary)
    TowerOfHanoi(n - 1, source, auxiliary, destination)
    print("to second: ", source, destination, auxiliary)
    print ("Move disk", n, "from source", source, "to destination", destination)
    TowerOfHanoi(n - 1, auxiliary, destination, source)
    print("omg")


# Driver code
n = 3
TowerOfHanoi(n, 'A', 'B', 'C')
# A, C, B are the name of rods

# Contributed By Dilip Jain