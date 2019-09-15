import pandas as pd
import nlp

df = pd.DataFrame(columns = ['Time', 'Emergency', 'Dispatch', 'Address', 'Alert'])

#for dep in ['f', 'p', 'g']:
for dep in ['p']:
    for unit in range(1, 4):
        with open(f'../audio/{dep}{unit}.csv', 'r') as fi:
            lines = fi.readlines()
            for line in lines:
                sp = ''.join(line.split(',')[1:])
                if len(sp) > 3:
                    a, b, c = nlp.parse_sentance(sp, 39.051600, -77.174820)
                    if not (a is None and b is None and c is None):
                        print(sp)
                        print('\n')

                        df = df.append({'Time': int(line.split(',')[0]),
                                        'Emergency': a,
                                        'Dispatch': b,
                                        'Address': c,
                                        'Alert': sp[1]},
                                        ignore_index=True)

df = df.sort_values('Time')
df.to_csv('all.csv')
