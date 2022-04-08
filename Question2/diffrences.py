import os
import argparse
import pandas as pd
from openpyxl import load_workbook


def get_sheets_diff(xlsx_file_name, sheet1, sheet2, column):
    '''
    it take path of an xlsx file 2 sheet pages and the target column and return their diference
    '''
    if not os.path.isfile(xlsx_file_name):
        print(xlsx_file_name, "file not found")
        exit()
    excel_data = pd.ExcelFile(xlsx_file_name)
    sorted_surname_list_1 = pd.read_excel(
        excel_data, sheet1).sort_values(by=column)[column]
    sorted_surname_list_2 = pd.read_excel(
        excel_data, sheet2).sort_values(by=column)[column]
    return pd.concat([sorted_surname_list_1, sorted_surname_list_2]).drop_duplicates(keep=False)


def add_new_sheet(xlsx_file_name, content, sheet3):
    '''
    it take path of an xlsx file and data and write it to new sheet page
    '''
    if not os.path.isfile(xlsx_file_name):
        print(xlsx_file_name, "file not found")
        exit()
    book = load_workbook(xlsx_file_name)
    writer = pd.ExcelWriter(xlsx_file_name, engine='openpyxl')
    writer.book = book
    content.to_excel(writer, sheet_name=sheet3, index=False)
    writer.save()
    writer.close()


parser = argparse.ArgumentParser(
    description='Find the differences between the 2 lists by generating a 3rd list which contains only those elements from every list.')

parser.add_argument("-f", "--file-xls",
                    help="supply challenge xlsfile", default="Lists.xlsx")

parser.add_argument("-l1", "--list1-sheet",
                    help="the name of the sheet 1 in the xlsx file", default="List 1")

parser.add_argument("-l2", "--list2-sheet",
                    help="the name of sheet 2 in the xlsx file", default="List 2")

parser.add_argument("-c", "--column",
                    help="column name in  xlsx file", default="Surname")

args = parser.parse_args()
config = vars(args)

lists_differences = get_sheets_diff(
    config['file_xls'], config['list1_sheet'], config['list2_sheet'], config['column'])
add_new_sheet(config['file_xls'], lists_differences, 'List 3')
