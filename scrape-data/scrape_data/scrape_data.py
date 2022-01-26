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
	'Native American/Alaskan',
	'Not Available'
]

def convert_xls_to_csv(xls_filename):
	read_file = pd.read_excel(xls_filename)
	xls_filename_without_extension = xls_filename.split('.')[0]
	csv_filename = f'{xls_filename_without_extension}.csv'
	read_file.to_csv(csv_filename, index=None, header=True)

def convert_many_xls_to_csv(file_directory, file_path):
	file_count = 0
	for file in file_directory:
		print(f'file: {file}')
		extension = os.path.splitext(file)[-1].lower()
		file_with_path = os.path.join(file_path, file)
		if os.path.isfile(file_with_path) and (extension == '.xls' or extension == '.xlsx'):
			print(f'file to be converted: {file_with_path}')
			convert_xls_to_csv(file_with_path)
			file_count += 1
	print(f'{file_count} files converted')

def check_row(row, year_one, year_two):
	if all(x == '' for x in row):
		return False, year_one, year_two
	if any((x == 'N' or x == '%') for x in row):
		return False, year_one, year_two
	if row[0].startswith('Unnamed') or row[0].startswith('NOTE:'):
		return False, year_one, year_two
	if row[2].startswith('20') and row[2] != '20':
		year_one = row[2][:4]
		year_two = row[8][:4]
		return False, year_one, year_two
	return True, year_one, year_two


def convert_racial_ethnic_csv_to_dict(csv_filename, racial_categories):
	year_one = None
	year_two = None
	if racial_categories == {}:
		for category in RACIAL_ETHNIC_CATEGORIES:
			racial_categories[category] = set()

	with open(csv_filename) as csvfile:
		csv_reader = csv.reader(csvfile)
		for row in csv_reader:
			data_to_be_added, year_one, year_two = check_row(row, year_one, year_two)
			if data_to_be_added:
				# rows with data we want
				category_name = row[0]
				if category_name == '':
					continue
				year_one_number = row[2]
				year_one_percent = row[3]
				year_two_number = row[8]
				year_two_percent = row[9]

				if category_name != '':	
					racial_categories[category_name].add((year_one, year_one_number, year_one_percent))
					racial_categories[category_name].add((year_two, year_two_number, year_two_percent))


def convert_many_racial_ethnic_csv_to_dict(file_directory):
	racial_categories = {}
	for file in file_directory:
		extension = os.path.splitext(file)[-1].lower()
		file_with_path = os.path.join(FILE_PATH, file)
		if (file.startswith(RACIAL_ETHNIC_PREFIX) 
			and os.path.isfile(file_with_path) 
			and (extension == '.csv')):
			convert_racial_ethnic_csv_to_dict(file_with_path, racial_categories)

	print(racial_categories)



def main():
	print('this is a data wrangling script that could be named better.')
	file_directory = os.listdir(FILE_PATH)

	# conversion only needs to be done once
	# convert_many_xls_to_csv(file_directory, FILE_PATH)

	convert_many_racial_ethnic_csv_to_dict(file_directory)




if __name__ == '__main__':
	main()