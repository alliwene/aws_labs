import pandas as pd 
import random

df = pd.read_excel('Groups.xlsx')

names = list(df['Name'].copy().values)
random.Random(4).shuffle(names)
members = 4
final = {} 

for i in range((len(names) // members) + 1):
    group = names[i*members:(i*members + members)]
    for item in group: 
        final[item] = i + 1

df['Group'] = df['Name'].map(final)
df.to_csv('groups_assigned.csv', index=False) 
