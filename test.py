MAX_STARS = 5

for i in range(5, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()

# print a full pyramid
n = 5
for i in range(n):
    print(" " * (n - i - 1), end="")
    print("* " * (i + 1))  

# print a full pyramid with spaces between stars
for i in range(MAX_STARS):
    print(" " * (MAX_STARS - i - 1), end="")
    for j in range(i + 1):
        print("* ", end="")
    print()

print()

# print an inverted pyramid
for i in range(MAX_STARS):
    for j in range(0, i, 1):
        print(" ", end="")
    for k in range(MAX_STARS, i, -1):
        print("* ", end="")
    print()

print() 

# print a diamond shape
# pyramid
for i in range(MAX_STARS):
    print(" " * (MAX_STARS - i - 1), end="")
    for j in range(i + 1):
        print("* ", end="")
    print()
# inverted pyramid
for i in range(MAX_STARS):
    for j in range(0, i + 1, 1):
        print(" ", end="")
    for k in range(MAX_STARS - 1, i, -1):
        print("* ", end="")
    print()

print()

# Pine Tree NOT COMPLETE
for i in range(MAX_STARS):
    for j in range(MAX_STARS, i, -1):
        print(" ", end="")
    for k in range(0, i + 1, 1):
        print("* ", end="")
    print()
