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
	df['Station'] = df['Week'].apply(week_to_station)
	df = df.drop(['Week'], axis=1)
	dfGroupBy = df.groupby(['State', 'Year', 'Station'])

	# Max Feature
	dfMax = dfGroupBy.max()
	dfMax.to_csv('data/features/ResultsMax.csv')

	# Min Feature
	dfMin = dfGroupBy.min()
	dfMin.to_csv('data/features/ResultsMin.csv')

	# Mean Feature
	dfMean = dfGroupBy.mean()
	dfMean.to_csv('data/features/ResultsMean.csv')

	# Mean Feature
	dfStd = dfGroupBy.std()
	dfStd.to_csv('data/features/ResultsStd.csv')

	# Custom Feature
	dfCustom = dfGroupBy.agg([custom_aggregation])
	dfCustom.to_csv('data/featuresResultsCustom.csv')