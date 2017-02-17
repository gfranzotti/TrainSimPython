import xlrd
book = xlrd.open_workbook("teste.xlsx")
sh = book.sheet_by_index(0)
print("Valor da célula D4 é ", sh.cell_value(rowx=3, colx=3))
print("Valor da célula B2 é ", sh.cell_value(rowx=1, colx=1))
print("Valor da célula A1 é ", sh.cell_value(rowx=0, colx=0))
print("Valor da célula C3 é ", sh.cell_value(rowx=2, colx=2))
print(sh.name, sh.nrows, sh.ncols, book.sheet_names(), book.nsheets)
