# inventory count less than 10

from openpyxl.reader.excel import load_workbook

inventory_workbook = load_workbook("inventory.xlsx")
products_list = inventory_workbook["Sheet1"]
#print(products_list)   #<Worksheet "Sheet1">

product_inventory={}

for product_row in range(2,products_list.max_row+1):
    #print(product_row)
    price = products_list.cell(product_row,3).value
    inventory = products_list.cell(product_row,2).value
    product_num = products_list.cell(product_row,1).value
    cell_to_added = products_list.cell(product_row,5)
    cell_to_added.value = price*inventory

inventory_workbook.save("inventory_updated_with_total.xlsx")