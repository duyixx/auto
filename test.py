import openpyxl

workbook = openpyxl.load_workbook("./test.xlsx")
sheet = workbook["register"]
print(sheet.cell(1,1).value)
for i,x in enumerate(["a","b","c"]):
    print(i,x)
