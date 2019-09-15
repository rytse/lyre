from ibm_watson import NaturalLanguageUnderstandingV1
print('Back-end started!')
import time
while(1):
    time.sleep(100)
    with open("be.txt",'w') as f:
        f.write('Back-end running!\n')
    print('foo')