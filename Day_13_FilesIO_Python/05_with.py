# 1st way of writing it
# with is known as context manager
# with open("tanzim.txt", "r") as f:
#     for line in f:
#         print(line)
# No need to explicitly close the file; it's done automatically

#2nd way of writing it

with open("tanzim.txt", "r") as f:
    content = f.read()
    print(content)
# No need to explicitly close the file; it's done automatically