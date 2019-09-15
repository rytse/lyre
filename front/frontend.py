print('Front-end started!')
import time
while(1):
    time.sleep(100)
    with open("fe.txt",'w') as f:
        f.write('Front-end running!\n')