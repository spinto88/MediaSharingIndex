import pandas as pd
import numpy as np 

# Load users interactions
df = pd.read_csv('Users_interactions.csv')
# Remove self-retweets
df = df[df['uid'] != df['uid_rt']]

# MSI users
msi_users = pd.read_csv('../Data/MSI_users.csv')

# Merge data of users interactions with msi of the users
df = df.merge(msi_users, left_on = 'uid', right_on = 'uid')
df = df.merge(msi_users, left_on = 'uid_rt', right_on = 'uid')

df.drop(columns = ['uid_y'], inplace = True)
df.columns = ['uid', 'uid_rt', 'msi_uid', 'msi_uid_rt']

# Average of score of target users
df.groupby('uid_rt').mean()[['msi_uid','msi_uid_rt']].to_csv('Average_score_targets_users.csv')
