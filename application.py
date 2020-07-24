import csv
def create_csv_file():
  records = [
      {'FEE': '£106m', 'YEAR': '2018', 'NAME': 'PHILIPPE COUTINHO', 'TO': 'BARCELONA', 'FROM': 'LIVERPOOL'},
      {'FEE': '£89m', 'YEAR': '2016', 'NAME': 'PAUL POGBA', 'TO': 'MAN UTD', 'FROM': 'JUVENTUS'},
      {'FEE': '£89m', 'YEAR': '2019', 'NAME': 'EDEN HAZARD', 'TO': 'REAL MADRID', 'FROM': 'CHELSEA'},
      {'FEE': '£86m', 'YEAR': '2013', 'NAME': 'GARETH BALE', 'TO': 'REAL MADRID', 'FROM': 'SPURS'},
      {'FEE': '£80m', 'YEAR': '2009', 'NAME': 'CRISTIANO RONALDO', 'TO': 'REAL MADRID', 'FROM': 'MAN UTD'},
      {'FEE': '£80m', 'YEAR': '2019', 'NAME': 'HARRY MAGUIRE', 'TO': 'MAN UTD', 'FROM': 'LEICESTER CITY'},
      {'FEE': '£75m', 'YEAR': '2018', 'NAME': 'VIRGIL VAN DIJK', 'TO': 'LIVERPOOL', 'FROM': 'SOUTHAMPTON'},
      {'FEE': '£75m', 'YEAR': '2014', 'NAME': 'LUIS SUAREZ', 'TO': 'BARCELONA', 'FROM': 'LIVERPOOL'},
      {'FEE': '£75m', 'YEAR': '2017', 'NAME': 'ROMELU LUKAKU', 'TO': 'MAN UTD', 'FROM': 'EVERTON'},
      {'FEE': '£74m', 'YEAR': '2019', 'NAME': 'ROMELU LUKAKU', 'TO': 'INTER MILAN', 'FROM': 'MAN UTD'},
  ]
  csv_writer = csv.writer(open('record.csv', 'w'), delimiter=',')
  csv_writer.writerow(['FEE', 'YEAR', 'NAME', 'TO', 'FROM'])
  for record in records:
      csv_writer.writerow([record['FEE'], record['YEAR'], record['NAME'], record['TO'], record['FROM']])

#def read_csv_file():
  #for row in csv.reader(open('record.csv','r'), delimiter=','):
   #if len(row) > 0:
      #print(row[0]+' '+row[1]+' '+row[2]+' '+row[3]+' '+row[4])

#def update_csv_ile():
  #csv_writer = csv.writer(open('record.csv', 'a'), delimiter=',')
  #csv_writer.writerow(['FEE', 'YEAR', 'NAME', 'TO', 'FROM'])
if __name__ == "__main__":
    create_csv_file()
    #read_csv_file()
    #update_csv_file()
