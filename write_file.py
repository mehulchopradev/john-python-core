with open('/Users/mehul.chopra/Documents/john', mode='wt') as fp:
  fp.write('First line\n')
  fp.write('Second line\n')
  s = ('mehul', 'm', 10)
  fp.write(str(s))