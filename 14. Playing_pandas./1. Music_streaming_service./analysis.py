import pandas as pd

songs = pd.read_csv('./songs.csv')
listens = pd.read_csv('./listens.csv').sort_values(by='user_id')
users = pd.read_csv('./users.csv')

data = pd.merge(listens, users, on = 'user_id')
data = pd.merge(data, songs, how='outer', on='song_id')


data = data[data['subscription_type'] == 'premium']
genre_list = list(set(data['genre']))

hash_map = {}

for genre in genre_list:
	hash_map[genre] = {}
	
	for row in data[data['genre'] == genre].iterrows():
		if row[0] in hash_map[genre]:
			hash_map[genre][row[0]] += 1
		else:
			hash_map[genre][row[0]] = 1		

for genre in genre_list:
	print(genre, ":", sorted(hash_map[genre].items(), key=lambda x:x[1])[:3])

