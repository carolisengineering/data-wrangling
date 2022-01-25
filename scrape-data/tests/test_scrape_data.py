import os

from tests.constants import (
    NUMBER_OF_XLS_TEST_FILES, 
    NUMBER_OF_XLSX_TEST_FILES,
)

from scrape_data import __version__
from scrape_data.scrape_data import (
    convert_xls_to_csv, 
    convert_many_xls_to_csv,
)


def count_file_types(list_of_files):
    xls_count = 0 
    xlsx_count = 0 
    csv_count = 0

    for filename in list_of_files:
        if filename.endswith('.xlsx'):
            xlsx_count += 1
        elif filename.endswith('.xls'):
            xls_count += 1
        elif filename.endswith('.csv'):
            csv_count += 1
    return xls_count, xlsx_count, csv_count



def test_version():
    assert __version__ == '0.1.0'

def test_convert_to_csv():
    file_path = 'tests/files'
    file_directory = os.listdir(file_path)
    starting_file_count = NUMBER_OF_XLS_TEST_FILES + NUMBER_OF_XLSX_TEST_FILES
    xls_count = 0
    xlsx_count = 0
    csv_count = 0

    assert starting_file_count == len(file_directory)
    
    xls_count, xlsx_count, csv_count = count_file_types(file_directory)

    assert xls_count == NUMBER_OF_XLS_TEST_FILES
    assert xlsx_count == NUMBER_OF_XLSX_TEST_FILES
    assert csv_count == 0

    convert_many_xls_to_csv(file_directory, file_path)

    new_file_directory = os.listdir(file_path)
    new_xls_count, new_xlsx_count, new_csv_count = count_file_types(new_file_directory)

    assert new_csv_count == new_xls_count + new_xlsx_count
