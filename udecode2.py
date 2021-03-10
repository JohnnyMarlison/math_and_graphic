# -*- coding: utf-8 -*-
'''
------------------------------------------------------------
Однозначная декодируемость кодов: использование
алгоритма Ал.А. Маркова на основе графов
------------------------------------------------------------
'''
codeTable = {'А': '00', 'Б': '01', 'В': '100',
             'Г': '10', 'Д': '110' }

codeTable = {'А': '0', 'Б': '11', 'В': '010' }

codeTable = {'А': '01', 'Б': '010', 'В': '011',
             'Г': '11', 'Д': '101' }
codeTable = {'А': '100', 'Б': '101', 'В': '111',
             'Г': '110', 'Д': '00' }

codeTable = {'А': '00', 'Б': '01', 'В': '100',
             'Г': '10', 'Д': '110', 'Е': '111' }

codeTable = {'А': '01', 'Б': '010', 'В': '011',
             'Г': '11', 'Д': '101' }

codeTable = {'А': '10', 'Д': '011', 'Л': '1011',
             'Ж': '1110', 'Т': '0' }

codeTable = {'A': '10', 'B': '1010', 'C': '101010' }

print("Исходная кодовая таблица")          
print("    " + str(codeTable))
'''
------------------------------------------------------------
Функция getSymByCode
------------------------------------------------------------
'''
def getSymByCode(code, bWithCode = False):
   '''
   Функция getSymByCode возвращает символ из кодовой
   таблицы, код которого совпадает с первым параметром.
   Если второй параметр отличен от 0, справа через
   двоеточие дописывается код символа.
   '''
   for (k,v) in codeTable.items():
       if code == v:
          if bWithCode:
                return k + ':' + code
          else: return k
   return code  
def checkLambda ( s ):
   if type(s) == list:
     sLam = s[:] 
     for i, word in enumerate(s):
        sLam[i] = checkLambda(word)
     return sLam   
   else:         
     if s == '': return "Lambda" 
     else: return s     
'''
------------------------------------------------------------
Выделение вершин графа Ал.А. Маркова
Вершинами графа становятся кодовые последовательности, которые:
1) не совпадают ни с одним кодовым словом
2) совпадают с началом и концом каких-то кодовых слов
------------------------------------------------------------
'''
nodes = ['']                        # список вершин графа
                                    # '' = Lambda
vals = list(codeTable.values())     # список кодов
maxLen = max(list(map(len, vals)))  # максимальная длина кода

for lenx in range(1,maxLen):        # по всем кодам длины от 1 до msxLen-1
    fmt = "{0:0" + "{0:d}".format(lenx) + "b}"
    for x in range(2**lenx):          # по всем x от 0 до 2^lenx-1
        code = fmt.format(x)          # формат преобразования в строку
        if not code in vals:          # такого кода нет
           bStarts = any(list(map(lambda x: x.startswith(code), vals)))
           bEnds = any(list(map(lambda x: x.endswith(code), vals)))
           if bStarts & bEnds:             # если есть совпадение с началом и концом каких-то кодов
               nodes.append(code)            # добавить узел в список
print("Вершины графа Ал.А. Маркова\n    ", end="")
print(checkLambda(nodes))
'''
------------------------------------------------------------
Построение списков смежности для вершин графа
Словарь "имя вершины: список смежности"
Список смежности состоит из 3-элементных кортежей
вида (конечная вершина, промежуточный код, получаемый код)
------------------------------------------------------------
'''
# строковая запись вершин
nodeStr = {}  
for node in nodes:        
    nodeStr[node] = '' if node == "Lambda" else node
# сложный вариант того же самого:
#   nodeStr = dict(zip(nodes,map(lambda x: x if x != "Lambda" else '', nodes)))

#------------------------------------------------------------
# Построение промежуточных кодов по маске:
# Список кодовых слов: ["10", "11", "111"] 
# Маска: "010"
# Результат: "11"
#-----------------------------------------------------------
def middleCodes ( codeWords, mask ):
   middle = []
   for i, b in enumerate(mask):
      if b == "1": middle.append(codeWords[i])
   return middle   
#-----------------------------------------------------------
# Двоичная запись числа заданной длины
#-----------------------------------------------------------
def binStr ( n, length ):
   s = bin(n)[2:];
   return "0"*(length-len(s)) + s

'''
------------------------------------------------------------
Построение всех возможных цепей вида
 префикс-код1-код2-...-суффикс
Отбор тех их них, которые совпадают с другими кодовыми словами
(циклов).
-----------------------------------------------------------
'''
nodeNext = {}
def generateAll ( prefix, middle, suffix ):
   newVal = prefix + "".join(middle) + suffix;
   # print(newVal, prefix, middle, suffix)
   if len(newVal) > maxLen: return
   if newVal in vals and \
      not (prefix == '' and len(middle) == 1 and suffix == ''):
     nodeNext[prefix].append((suffix, middle, newVal))
   for v in vals:
      newMiddle = middle[:]
      newMiddle.append(v)
      generateAll ( prefix, newMiddle, suffix )

for prefix in nodes:
  nodeNext[prefix] = []
  for suffix in nodes:
     generateAll ( prefix, [], suffix )
'''
------------------------------------------------------------
Вывод списка дуг графа Ал.А. Маркова
------------------------------------------------------------
'''
print("Дуги графа")          
for prefix in nodeNext:
  netList = nodeNext[prefix]
  for edge in netList:
    suffix, middle, result = edge
    print("    " + checkLambda(prefix) + ' -> ', end="")
    for v in middle:
      v = checkLambda(v)
      print ( '(' + getSymByCode(v,True) + ')', end=""); 
    print(' -> ' + checkLambda(suffix) + ' = ' + getSymByCode(result,True))
'''
------------------------------------------------------------
Поиск циклов, проходящих через вершину "Lambda"
------------------------------------------------------------
'''
allLoops = [] # список для хранения данных о найденных циклах
visited = {}
# for k in nodeNext: visited[k] = False
# сложный вариант того же самого:
# visited = dict(zip(nodeNext,[False]*len(nodeNext))) # флаги посещения вершин
'''
------------------------------------------------------------
Функция findLambdaLoops
------------------------------------------------------------
'''
def findLambdaLoops(curNode, curPath):
    '''
    Функция выполняет поиск циклов, которые заканчиваются
    на вершине "Lambda".
    Используются глобальные массивы
      allLoops - список всех найденны циклов в графе
      visited  - словарь, соджержащий флаги посещения
                 для каждой вершины
    '''
    if curPath and curNode == "": # цикл замкнулся
        allLoops.append(curPath[:])
        return

    if visited.get(curNode,False): return

    visited[curNode] = True;
    nextNodeList = nodeNext[curNode]
    for edge in nextNodeList:
         toNode, middle, result = edge
         curPath.append((toNode, middle, result)) 
         findLambdaLoops(toNode, curPath)
         curPath.pop()
         
    visited[curNode] = False

findLambdaLoops("", [])  # ищем пути из вершины Lambda
'''
------------------------------------------------------------
Вывод циклов, проходящих через вершину "Lambda",
и кодовых последовательностей, которые декодируются
неоднозначно
------------------------------------------------------------
'''
if len(allLoops) > 0:
    print('Обнаружены циклы:')
    for loop in allLoops:
        print('    Lambda',end='')
        binStr = ""
        decode1 = ""
        decode2 = ""
        n = 1
        for edge in loop:
            print(' ->', checkLambda(edge[0]), end='')
            for m in edge[1]: binStr += m               
            if edge[0] != "":
              binStr += edge[0]
            if n == 1:
              for m in edge[1]:
                 decode1 += getSymByCode(m)
              decode2 += getSymByCode(edge[2])
            if n == 2:
               for m in edge[1]:
                  decode2 += getSymByCode(m)
               decode1 += getSymByCode(edge[2])
            n = 3 - n
        print(": " + binStr, "=>", decode1, "=", decode2)       
else:
    print('Циклов не обнаружено.')


    

