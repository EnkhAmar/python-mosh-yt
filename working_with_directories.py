from pathlib import Path

path = Path()   # current directory
# print(path.glob('*.py'))      # generator object

for file in path.glob('*'):
    print(file)







# Absolute path
# c:\Program Files\Microsoft
# /usr/local/bin

# Relative path