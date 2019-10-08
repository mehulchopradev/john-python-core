with open('/Users/mehul.chopra/Documents/professor.py') as file_obj:
  for line in file_obj:
    print(line.rstrip())

# when the program flow comes out of the with block, the file_obj resource acquired in the with block will be
# automatically released(closed)