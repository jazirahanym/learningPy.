
f = open('Dovlatov.Nashy', 'r')

import re 

s = ['выпила', 'выпил','выпить','выпили','выпивал','выпьют', 'выпивали'] 
w = [0,0,0,0,0,0,0]

#читаем файл построчно
for line in f.readlines(): 
      #преобразовать в маленькие буквы
      line = line.lower() 

      i = 0 
      for a in s: 
          #Вот регулярное выражнение, которое ищет глагол
          match = re.search( r'\b%s\b' %(a), line) 
          if match:
             w[i] = w[i] + 1 
          i = i + 1
      
i = 0
for a in s:
    print(a, w[i])
    i = i + 1
      
f.close() 
