import camelot

tables = camelot.read_pdf('June Bank Statement.PDF', pages='all', flavor='stream')

for table in tables:
    table.to_csv('junestatement.csv', mode='a')
