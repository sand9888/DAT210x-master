import pandas as pd


# TODO: Load up the table, and extract the dataset
# out of it. If you're having issues with this, look
# carefully at the sample code provided in the reading
df = pd.read_html('http://www.espn.com/nhl/statistics/player/_/stat/points/sort/points/year/2015/seasontype/2')[0]


'''df = df.dropna(axis=0, thresh = 4)
df.columns = df.iloc[0]
df=df[1:]
df = df.drop(labels = 'RK', axis=1)
df = df.reset_index(drop=True)
print(df.PCT.unique())
print(df.ix[15:16, 'GP'])'''


# TODO: Rename the columns so that they are similar to the
# column definitions provided to you on the website.
# Be careful and don't accidentially use any names twice.
df.columns = ['RK',	'PLAYER','TEAM','GP','G1','A1','PTS','+/-','PIM','PTS/G','SOG','PCT','GWG','G2','A2',	'G3',	'A3']
df = df.set_index('RK')
df = df.drop(labels='RK', axis = 0)
df = df.reset_index(drop=True)



# TODO: Get rid of any row that has at least 4 NANs in it,
# e.g. that do not contain player points statistics
df = df.dropna(axis=0, thresh = 4)
df = df.reset_index(drop=True)
print(df)


# TODO: At this point, look through your dataset by printing
# it. There probably still are some erroneous rows in there.
# What indexing command(s) can you use to select all rows
# EXCEPT those rows?
#
# .. your code here ..


# TODO: Get rid of the 'RK' column
#
# .. your code here ..


# TODO: Ensure there are no holes in your index by resetting
# it. By the way, don't store the original index
#
# .. your code here ..



# TODO: Check the data type of all columns, and ensure those
# that should be numeric are numeric
df['GP'] = pd.to_numeric(df['GP'], errors='coerce')
df['G1'] = pd.to_numeric(df['G1'], errors='coerce')
df['A1'] = pd.to_numeric(df['A1'], errors='coerce')
df['PTS'] = pd.to_numeric(df['PTS'], errors='coerce')
df['+/-'] = pd.to_numeric(df['+/-'], errors='coerce')
df['PIM'] = pd.to_numeric(df['PIM'], errors='coerce')
df['PTS/G'] = pd.to_numeric(df['PTS/G'], errors='coerce')
df['SOG'] = pd.to_numeric(df['SOG'], errors='coerce')
df['GWG'] = pd.to_numeric(df['GWG'], errors='coerce')
df['G2'] = pd.to_numeric(df['G2'], errors='coerce')
df['A2'] = pd.to_numeric(df['A2'], errors='coerce')
df['G3'] = pd.to_numeric(df['G2'], errors='coerce')
df['A3'] = pd.to_numeric(df['A2'], errors='coerce')



print(df.shape)
print(len(df.PCT.unique()))
print(df.ix[15:16, 'GP'])



# TODO: Your dataframe is now ready! Use the appropriate 
# commands to answer the questions on the course lab page.
#
# .. your code here ..

