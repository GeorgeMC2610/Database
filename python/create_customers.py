f = open('CONTRACTS2.sql', 'r')
lines = f.read()
lines = lines.split('\n')
f.close()

f = open('CUSTOMERS.sql', 'r')
lines_2 = f.read()
lines_2 = lines_2.split('\n')
f.close()

new_file = open('CUSTOMERS2.sql', 'a')

for i in range(0, 500):
    previous_query  = lines[i].replace(',', '')
    previous_query  = previous_query.split()
    email           = previous_query[16]
    contract_number = previous_query[11].strip('()')
    query = lines_2[i]
    query = query.replace("'email',", email + ",")
    query = query.replace("'contract');", contract_number + ");")
    print(query)
    new_file.write(query + '\n')

new_file.close()

'''query = "insert into CONTRACTS (number, category, starting_date, end_date, price, CUSTOMER_email, VEHICLES_plates) values (48715563, 'Mixed', '1990-06-25', '2039-06-16', 7886, 'gcusick16@businessinsider.com', 'BMB - 6567');"
query = query.replace(',', '')
query = query.split()
print(query)'''