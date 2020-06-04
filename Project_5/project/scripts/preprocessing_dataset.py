import pandas as pd

def select_positions(data):
	valid_positions = ['CF', 'LW', 'RW', 'CM', 'LM', 'LWB', 
			   'LB', 'RM', 'RWB', 'RB', 'GK']
	data = data[data['Position'].isin(valid_positions)]
	return data

def remove_players_with_K_salary(data):
	data = data[~data['Release Clause'].str.endswith('K')]
	return data

def convert_salary2num(data):
	data['Release Clause'] = [val[1:-1] for val in data['Release Clause']]
	return data		

if __name__ == '__main__':
	filename = 'data.csv'
	
	# read data
	df = pd.read_csv(filename, header=0)
	df = select_positions(df)
	df = remove_players_with_K_salary(df)
	df = convert_salary2num(df)
	# shuffle data and take 300 rows
	df = df.sample(frac=1)
	df = df[:300]
	# save to file
	df.to_csv('small_data.csv', index=False)
