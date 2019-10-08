from csv import reader, writer, DictWriter

path = '/Users/mehul.chopra/Documents/personal/training/data-analysis-data/weather_data_input/weather_data_set_1900'

with open(path) as fp:
  reader_obj = reader(fp, delimiter='|')
  with open('/Users/mehul.chopra/Desktop/year_temp.csv', mode='wt') as fd:
    # writer_obj = writer(fd)
    writer_obj = DictWriter(fd, fieldnames=['Year', 'Temperature'])
    writer_obj.writeheader()

    for line in reader_obj:
      print('Year: {0}\nTemp: {1}'.format(line[1], line[4]))
      # writer_obj.writerow([line[1], line[4]])
      writer_obj.writerow({'Year': line[1], 'Temperature': line[4]})
