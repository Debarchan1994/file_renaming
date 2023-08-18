import os
import pandas as pd
import numpy as np

# path to the files

path = r'path_of_the_directory_containing_the_files_to_be_renamed'

# stand base name for the files specific to a certain type of task

basename = str('your_base_commaon_extension_to_every_file')
# path_save = r''

num_files = len(next(os.walk(path))[2])
print(num_files)

length = list(range(1, num_files+1))
print(length)

count = 0
flag = 0 

df = pd.DataFrame(columns=['new_name', 'old_name'])

for i in os.listdir(path):
    
    if os.path.isfile(os.path.join(path, i )):
    
        name = i.split('.')
        print(name)
        if basename in name[0]:
            flag = flag + 1
            print(name[0].split(basename))
            digit = int(name[0].split(basename)[1])
            if digit in length:
                length.remove(digit)
                length.append(length[-1] + 1)
            else:
                pass

    
for i in os.listdir(path):
    
    if os.path.isfile(os.path.join(path, i )):
    
        name = i.split('.')
        if basename in name[0]:
            pass
        else:
            os.rename('{}'.format(os.path.join(path , i)), '{}'.format(os.path.join(path, '{}{}.{}'.format(basename,str(length[count]), name[-1]))))
            
            df = df._append({'new_name': '{}{}.{}'.format(basename, str(length[count]), name[-1]), 'old_name': i}, ignore_index=True)
            df = df._append({'new_name': np.nan , 'old_name': np.nan}, ignore_index=True)
            count = count + 1
            
            
    # print(i.split('.'))
    # break
    else:
        pass
    
# csv file created with new and old names of the files

df.to_csv(os.path.join(path , 'demo.csv'), index=False)

print(length)
