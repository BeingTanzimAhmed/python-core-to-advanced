import os

print (os.listdir("c:/Users/Amman/OneDrive/Desktop/Python Course/18_Files/dir")) # Lists all files and directories in the specified path
 
current_dir = os.getcwd()
print("Current directory:", current_dir) # Get the current working directory

if os.path.exists("c:/Users/Amman/OneDrive/Desktop/Python Course/18_Files/dir"): # Check if a path exists
    print("The directory exists.")

# os.remove("c:/Users/Amman/OneDrive/Desktop/Python Course/18_Files/sample.txt") # Remove a file
# os.rmdir("c:/Users/Amman/OneDrive/Desktop/Python Course/18_Files/dir") # Remove an empty directory