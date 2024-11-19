import csv

with open('Bestseller - Sheet1.csv','r',encoding="utf-8") as file:
    csv_reader = csv.reader(file)
    headers = next(csv_reader)
    print(headers)

    sales_index = headers.index("sales in millions")
    title_index = headers.index("Book")  

    max_sales = 0
    best_selling_book = ""

    for row in csv_reader:
        sales = float(row[sales_index])  # Convierte el valor de ventas a float
        if sales > max_sales:
            max_sales = sales
            best_selling_book = row[title_index]  # Guarda el título del libro con más ventas

    print(f"El libro más vendido es '{best_selling_book}' con ventas de {max_sales} millones.")
