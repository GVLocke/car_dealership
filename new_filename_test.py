import os
# look in the backup folder for the latest file
path = "./backup"
files = os.listdir(path)
paths = [os.path.join(path, basename) for basename in files]
newest = max(paths, key=os.path.getctime)
newest = newest[10:]

# string without the extension
filename_without_extension = newest.split(".")[0]
# remove dealership from the string
filename_without_extension = filename_without_extension.split("up")[1]
number = int(filename_without_extension) + 1
new_filename = "backup" + str(number) + ".dat"
print(new_filename)