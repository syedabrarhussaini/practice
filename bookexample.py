import openpyxl
boo = openpyxl.load_workbook("C:\\Users\\Abrar\\Desktop\\booking.xlsx")
sheet = boo.active
cell = sheet.cell(row=1, column=1)
print(cell.value)
