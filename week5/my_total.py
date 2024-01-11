import sys

count = len(sys.argv)

if count <= 1:
    print("No arguments were provided.")
else:
    total = 0
    for arg in sys.argv[1:]:
        total += float(arg)

    average = total / (count - 1)

    print("Total is", total)
    print("Average is", average)
