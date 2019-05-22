import pandas as pd 
df1 = pd.read_excel('Ab_Words_NAE_Tags.xlsx')
df1_train= df1.sample(n=844)
df1_dev= df1.sample(n=200)
df1_test= df1.sample(n=1)
df1_train.to_excel('train.xlsx')
df1_dev.to_excel('dev.xlsx')
df1_test.to_excel('test.xlsx')