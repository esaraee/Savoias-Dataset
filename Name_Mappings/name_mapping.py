#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 16:41:04 2018

@author: elham
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 14:26:08 2018

@author: elham
"""

import glob
import os

category = '200_ad'
data_dir = '/Users/elham/Downloads/'+ category+'/'
img_list = glob.glob(data_dir+'*.jpg')
print (img_list)
orig_names = [os.path.basename(x) for x in img_list]
import pandas as pd
from pandas import ExcelWriter

new_names = []
for i in range(len(img_list)):
    new_names.append(str(i)+'.jpg')
    
    
df = pd.DataFrame({'orig_names':orig_names, 'indices':new_names})
 
mapping_filename = '/Users/elham/Desktop/' + 'Ad' + '.xlsx'
writer = ExcelWriter(mapping_filename)
df.to_excel(writer,'Sheet1',index=False)
writer.save()
