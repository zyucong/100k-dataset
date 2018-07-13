import pandas as pd

# pandas.read_table() Read general delimited file into DataFrame
# set header as None to avoid using first line as header
data = pd.read_table(r'ml-100k/u.data', header = None)
data_df = pd.DataFrame(data)
data_df.columns = ['user id', 'item id', 'rating', 'timestamp']
user = pd.read_table(r'ml-100k/u.user', header = None, sep = '|')
user_df = pd.DataFrame(user)
user_df.columns = ['user id', 'age', 'gender', 'occupation', 'zip code']
# calculate the mean value of each user's rating
pivot = pd.pivot_table(data_df, values = 'rating', index = 'user id', aggfunc='mean')
# inner join two tables and keep only needed columns
merge = pivot.merge(user_df.loc[:,['user id', 'gender']], left_on = 'user id', right_on = 'user id', how = 'inner')
# calculate the standard deviation of the rating
male = merge[merge.gender == 'M'].rating.std()
female = merge[merge.gender == 'F'].rating.std()
print(f'The standard deviation of male is {male} \n'
      f'The standard deviation of female is {female}')
#The standard deviation of male is 0.4300759764233207 
#The standard deviation of female is 0.48124054201268524
