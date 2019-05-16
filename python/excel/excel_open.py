import xlrd
import xlwt
file = 'test.xlsx'
data = xlrd.open_workbook(file)

sheetNames = data.sheet_names()
print(sheetNames)
