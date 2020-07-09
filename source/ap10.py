
import os
os.chdir('/home/gopi/Python_202004/source')
import sys
sys.path.append('/home/gopi/Python_202004/source')

import reader

# Designing the 'interface' to solve the problem that we have 
reader0 = reader.XSV_Reader(separator=',')
data = reader0.read(r'/home/gopi/Python_202004/data/corona/ourworldindata/test_data.csv')
print(data.head())


reader1 = reader.XSV_Reader(separator=',')
data1 = reader1.read(r'/home/gopi/Python_202004/source/test.csv')
print(data1.head())
