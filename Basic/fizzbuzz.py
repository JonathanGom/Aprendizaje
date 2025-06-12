
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("\nFizzBuzz")
    elif i % 3 == 0:
        print("\nFizz")
    elif i % 5 == 0:
        print("\nBuzz")
    else:
        print("\n", i)