import random
import pandas as pd

df = pd.DataFrame()
df['t'] = range(100)

for dep in ['fire', 'police', 'guard']:
    for rep in range(5):
        xs = []
        ys = []

        x = 0
        y = 0
        dx = 0
        dy = 0
        for i in range(100):
            dx += random.random() * 2 - 1
            dy += random.random() * 2 - 1

            x += dx * 0.1
            y += dy * 0.1

            xs.append(x)
            ys.append(y)

        df[f'{dep}_{rep}_x'] = xs
        df[f'{dep}_{rep}_y'] = ys

df.to_csv('./all.csv')
