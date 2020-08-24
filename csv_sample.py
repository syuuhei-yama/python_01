import csv

#読み込み
with open('input.csv') as fh:
    csv_reader = csv.reader(fh, delimiter=',',quotechar='|')
    #for row in csv_reader:
    #   print(row)

#DictReader

#with open('input.csv') as fh:
#    csv_reader =  csv.DictReader(fh, delimiter=',',fieldnames=['name','age'])
#    csv_header = csv_reader.fieldnames
#    print(csv_header)
#    for row in csv_reader:
#        print(row['name'])

#writer
#with open('output.csv', mode='w', newline='') as fh:
#    csv_writer = csv.writer(fh, delimitre='/t')
#    csv_writer.writerows([['a','b','c'],[1,2,3]])

#DictWriter
with open('output.csv', mode='w', newline='') as fh:
    fieldnames = ['name','age']
    csv_writer = csv.DictWriter(fh, fieldnames=fieldnames)
    csv_writer.writeheader()
    csv_writer.writerow({'name':'Taro','age':19})
    csv_writer.writerows([{'name':'Hanako','age':30},{'name':'jiro','age':43}])



