import scrapy
import pandas as pd
import os, os.path
import csv

FILE_PATH = 'cpsdemographics/files/'
RACIAL_ETHNIC_PREFIX = 'demographics_racialethnic_'
RACIAL_ETHNIC_CATEGORIES = [
	'White',
	'African American',
	'Asian/Pacific Islander (retired)',
	'Native American',
	'Hispanic',
	'Multi-Racial',
	'Asian',
	'Hawaiian/Pacific Islander',
	'Not Available'
]

def convert_xls_to_csv(xls_filename):
	read_file = pd.read_excel(xls_filename)
	xls_filename_without_extension = xls_filename.split('.')[0]
	csv_filename = f'{xls_filename_without_extension}.csv'
	read_file.to_csv(csv_filename, index=None, header=True)

def convert_many_xls_to_csv(file_directory):
	file_count = 0
	for file in file_directory:
		print(f'file: {file}')
		extension = os.path.splitext(file)[-1].lower()
		print(extension)
		file_with_path = os.path.join(FILE_PATH, file)
		print(file_with_path)
		if os.path.isfile(file_with_path) and (extension == '.xls' or extension == '.xlsx'):
			print(f'file to be converted: {file_with_path}')
			convert_xls_to_csv(file_with_path)
			file_count += 1
	print(f'{file_count} files converted')

def convert_racial_ethnic_csv_to_dict(csv_filename):
	with open(csv_filename) as csvfile:
		csv_reader = csv.reader(csvfile)
		for row in csv_reader:
			if all(x == '' for x in row):
				continue
			if row[0].startswith('Unnamed:'):
				continue
			print(row)

def convert_many_racial_ethnic_csv_to_dict(file_directory):
	for file in file_directory:
		extension = os.path.splitext(file)[-1].lower()
		file_with_path = os.path.join(FILE_PATH, file)
		if (file.startswith(RACIAL_ETHNIC_PREFIX) 
			and os.path.isfile(file_with_path) 
			and (extension == '.csv')):
			convert_racial_ethnic_csv_to_dict(file_with_path)


def main():
	print('this is a data wrangling script that could be named better.')
	file_directory = os.listdir(FILE_PATH)

	# conversion only needs to be done once
	# convert_many_xls_to_csv(file_directory)

	convert_many_racial_ethnic_csv_to_dict(file_directory)




if __name__ == '__main__':
	main()