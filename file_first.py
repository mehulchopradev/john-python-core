file_obj = open('/Users/mehul.chopra/Documents/professor.py') # mode - rt
# print(type(file_obj))

# reading frm the file

print('Reading for the first time...')
# Efficient
for line in file_obj:
  print(line.rstrip())

# internal file pointer is still at the end of file

print('Reading for the second time...')
for line in file_obj:
  print(line.rstrip())

# reset the file pointer
file_obj.seek(0)
print('Reading for the third time...')
for line in file_obj:
  print(line.rstrip())

# internal file pointer is still at the end of file
file_obj.seek(0)

print('Reading all lines together..')
lines = file_obj.readlines()
# risk getting OOM issues
print(lines)

file_obj.seek(0)
print('Read as a string')
s = file_obj.read()
# riisk getting OOM issues
print(s)

file_obj.seek(0)

# once the work with the file is done, close the file
file_obj.close() # very important