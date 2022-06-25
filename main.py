def sorter(files, amount):
  library = {}
  for file in files:
    with open(file) as f:
      whole_text = f.read()
    with open(file) as f:
      library[file] = (len(f.readlines()), whole_text)
  sorted_library = sorted(library.items(), key=lambda x: x[1])
  for i in range(amount):
    with open('result.txt', 'a') as result:
      result.write(f'{sorted_library[i][0]}\n{sorted_library[i][1][0]}\n{sorted_library[i][1][1]}\n')
     

txts = ['1.txt', '2.txt', '3.txt']
sorter(txts, 3)
