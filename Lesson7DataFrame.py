import pandas as pd
df = pd.DataFrame()

list_4 = [1, 5, 45, 42, None, 123, 4213, None, 213]
df1 = pd.DataFrame(data = list_4)
print(df1)
print("---------------------------------------")

df2 = df1.dropna()
#print(df2)
print("---------------------------------------")
def divide2(x):
    return x/2
df3 = df2.apply(divide2)  # applies the function divide2 to all entries of the DataFrame

df3 = pd.DataFrame(data = df3)
print((df3))
