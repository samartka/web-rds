import pandas as pd

import sys
x=1500
sys.setrecursionlimit(x)

df = pd.read_json("https://kainoi.net/getdata.php?tb=tbcoupon")

df['wave'] = 0
df['seed_init'] = ''
df['chain'] = ''

df['c_lower'] = df['Coupon'].str.lower()
df['r_lower'] = df['Recruiter'].str.lower()



df = df[pd.isna(df['DateUsed'])==False]
df.reset_index(drop=True,inplace = True)

def find_seed(peer):
    global a
    a.insert(0,peer)
    if len(df['r_lower'][df['c_lower']== str(peer).lower()])== 0:
        return a
    else:
        find_seed(df['r_lower'][df['c_lower']==str(peer).lower()].values[0])

a = []
for index, row in df.iterrows():
    print(f'row number :  {index}')
    a.clear()
    find_seed(row['Coupon'])
    if str(a[0]) == 'None':
        a.pop(0)
    df.at[index,'wave']=len(a)-1
    df.at[index,'seed_init']=a[0]
    df.at[index,'chain']= ",".join(str(e) for e in a)

df.to_csv("network.csv",index=False)




