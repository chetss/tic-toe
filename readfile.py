import csv

with open('temp.csv', 'r') as csv_file:
    data = csv.reader(csv_file)

    for line in data:
        print(line)

mydict = {'index': [1, 2, 3, 4, 5, 6], 'price': [122, 12, 233, 444, 52, 222]}
with open('mytemp.csv', 'w') as csv2:
    csv_writier = csv.writer(csv2, delimiter=',')

    for key,value in mydict.items():
    	csv_writier.writerow([key,value])


# with open('mytemp1.csv','a') as f:
# 	[f.write('{0},{1}\n'.format(key,value)) for key, value in mydict.items()]