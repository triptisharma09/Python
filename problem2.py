import os

# Specify the directory you want to list,
# or leave it empty to list the current working directory
directory = "/Sonal"  # e.g., "C:/Users/You/Documents"

# Get the list of contents
contents = os.listdir(directory)  # Lists files + folders in the directory

# Print each entry
print(f"Contents of directory: {directory}")
for item in contents:
    print(item)
