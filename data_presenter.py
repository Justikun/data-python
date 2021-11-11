open_file = open('CupcakeInvoices.csv')
for invoice in open_file:
    invoice = invoice.split(',')
    print(invoice)

open_file.seek(0)

for invoice in open_file:
    invoice = invoice.split(',')
    print(invoice[2])

open_file.seek(0)

for invoice in open_file:
    invoice = invoice.split(',')
    print(float(invoice[4]))

open_file.seek(0)

sum = 0
for invoice in open_file:
    invoice = invoice.split(',')
    sum = sum + float(invoice[4]) 
print("Sum:", sum)

open_file.close()