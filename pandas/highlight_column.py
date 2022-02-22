import pandas as pd
df = pd.read_csv('abcd.csv')
highlight = lambda x: 'background-color: yellow'
display(df.style.applymap(highlight, subset=pd.IndexSlice[:, 'AbsDiff']))
