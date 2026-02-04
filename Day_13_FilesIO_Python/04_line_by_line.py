try:
    f = open("tanzim.txt", "r")

    for line in f:
        print(line)

    f.close()

except FileNotFoundError:   
    print("File not found. Please make sure the file exists.")