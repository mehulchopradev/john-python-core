from pathlib import Path
from shutil import copy2

source_file_path = input('Enter the absolute path of the file that needs to be copied : ')
dest_folder_path = input('Enter the destination folder where it needs to be copied : ')

# validate the source file path
# 1 It should exist
# 2 It should be path of a regular file
sp = Path(source_file_path)
dp = Path(dest_folder_path)

if sp.exists() and sp.is_file():
  # validate the destination path
  # 1 It should exist
  # 2 It should be path to a dir
  if dp.exists() and dp.is_dir():
    # extract name from the sps
    source_file_name = sp.name
    dest_file_path = "{0}/{1}".format(dest_folder_path, source_file_name)

    # start copying
    '''with open(source_file_path, mode='rb') as sfp:
      with open(dest_file_path, mode='wb') as dfp:
        for line in sfp:
          print(line)
          dfp.write(line)'''
    copy2(source_file_path, dest_folder_path)
    print('Copying done!')
  else:
    print('Invalid destination path')
else:
  print('Invalid source file path')