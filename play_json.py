from json import loads

path = '/Users/mehul.chopra/Documents/personal/training/data-analysis-data/url-shortner/usagov_bitly_data2012-03-16-1331923249.txt'

with open(path) as fp:
  for line in fp:
    line_obj = loads(line)
    print(type(line_obj))
