import os
import pandas as pd
import numpy as np

# path to the files

path = r'\\europe.bmw.corp\WINFS\Panama\PLW_FG_e1\BDP\AIBB\AcousticAnalytics\10_BusinessSolutions\EngineersShazam\40_Data\Technical-Service\Brake squeking noises CS region\G30 Brake squeking noises (G463542)\renamed'

# stand base name for the files specific to a certain type of task

basename = str('brknoise_techserv_G30_brk_G463542_')
# path_save = r'P:\C\CA_Bremse_FE\36_Bremse_Uebergreifend\Digitalisierung@Bremse\04_Products\09_Noise_Recognition\02_Messdaten\Technical_Service\Brake Noises DE\Bremsen Knarzen + Quietschen Videos\Renamed_data'

num_files = len(next(os.walk(path))[2])
print(num_files)

length = list(range(1, num_files+1))
print(length)

count = 0
flag = 0 

df = pd.DataFrame(columns=['new_name', 'old_name', 'human result', 'acan result', 'comment', 'model'])

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