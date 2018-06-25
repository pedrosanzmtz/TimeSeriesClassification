from sys import argv
import pandas as pd 


def week_to_station(week):
	if week >= 51 or week <= 11:
		return 'winter'
	if week >= 12 and week <= 25:
		return 'spring'
	if week >= 26 and week <= 34:
		return 'summer'
	if week >= 35 and week <= 50:
		return 'fall'


def custom_aggregation(x):
	m = x.mean()
	return 1 if(m >= 0.5) else 0


if __name__ == '__main__':
	file_name = argv[1]
	df = pd.read_csv(file_name)
	df = df.drop(['Men', 'Women'], axis=1)
	df['Station'] = df['Week'].apply(week_to_station)
	df = df[(df['Year'] <= 2016) & (df['Week'] <= 38)]
	df = df.drop(['Week'], axis=1)
	dfGroupBy = df.groupby(['State', 'Year', 'Station']).agg(['sum'])
	final = pd.concat([dfGroupBy['MenN'], dfGroupBy['WomenN']])
	dfGroupBy.to_csv('new_' + argv[1], index=False)
