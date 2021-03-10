#! /usr/bin/env python3
# -*- coding: utf-8 -*-

'''
------------------------------------------------------------
Однозначная декодируемость кодов: использование
алгоритма Ал.А. Маркова на основе графов
------------------------------------------------------------
'''
codeTable = {'А': '00', 'Б': '01', 'В': '100',
             'Г': '10', 'Д': '110'}

codeTable = {'А': '0', 'Б': '11', 'В': '010'}

codeTable = {'А': '01', 'Б': '010', 'В': '011',
             'Г': '11', 'Д': '101'}
print("Исходная кодовая таблица")
print("    " + str(codeTable))
'''
------------------------------------------------------------
Функция getSymByCode
------------------------------------------------------------
'''


def getSymByCode(code, bWithCode=False):
    '''
    Функция getSymByCode возвращает символ из кодовой
    таблицы, код которого совпадает с первым параметром.
    Если второй параметр отличен от 0, справа через
    двоеточие дописывается код символа.
    '''
    for (k, v) in codeTable.items():
        if code == v:
            if bWithCode:
                return k + ':' + code
            else:
                return k
    return code


'''
------------------------------------------------------------
Выделение вершин графа Ал.А. Маркова
Вершинами графа становятся кодовые последовательности, которые:
1) не совпадают ни с одним кодовым словом
2) совпадают с началом и концом каких-то кодовых слов
------------------------------------------------------------
'''
nodes = ['Lambda']  # список вершин графа
vals = list(codeTable.values())  # список кодов
maxLen = max(list(map(len, vals)))  # максимальная длина кода

for lenx in range(1, maxLen):  # по всем кодам длины от 1 до msxLen-1
    fmt = "{0:0" + "{0:d}".format(lenx) + "b}"
    for x in range(2 ** lenx):  # по всем x от 0 до 2^lenx-1
        code = fmt.format(x)  # формат преобразования в строку
        if code in vals: break  # такого кода нет
        bStarts = any(list(map(lambda x: x.startswith(code), vals)))
        bEnds = any(list(map(lambda x: x.endswith(code), vals)))
        if bStarts & bEnds:  # если есть совпадение с началом и концом каких-то кодов
            nodes.append(code)  # добавить узел в список
print("Вершины графа Ал.А. Маркова")
print("    ", nodes)
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

valsExt = vals[:]  # скопировать список кодов,
valsExt.append('')  # добавить значение Lambda

nodeNext = {}
for node1 in nodes:
    nodeNext[node1] = []
    for v in valsExt:
        for node2 in nodes:
            '''----------------------------------------------------
            Рассматриваются все комбинации
              вершина1 + код1 или Lambda + вершина2 = код2
            Ограничение:
              не рассматриваются цепочки с несколькими кодами
              в середине, например,
              вершина + код1 + код2 + ... + вершина2 = кодN
            ----------------------------------------------------'''
            newVal = nodeStr[node1] + v + nodeStr[node2]
            if not (node1 == 'Lambda' and node2 == 'Lambda') and newVal in vals:
                nodeNext[node1].append((node2, v, newVal))
# print(nodeNext)
'''
------------------------------------------------------------
Вывод списка дуг графа Ал.А. Маркова
------------------------------------------------------------
'''
print("Дуги графа")
for node1 in nodeNext:
    netList = nodeNext[node1]
    for edge in netList:
        node2, sym1, sym2 = edge
        if sym1 == '': sym1 = 'Lambda'
        print("    " + node1 + ' -> (' + getSymByCode(sym1, True) + ') -> ' + node2 + ' = ' + getSymByCode(sym2, True))
'''
------------------------------------------------------------
Поиск циклов, проходящих через вершину "Lambda"
------------------------------------------------------------
'''
allLoops = []  # список для хранения данных о найденных циклах
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
    if curPath and curNode == "Lambda":  # цикл замкнулся
        allLoops.append(curPath[:])
        return

    if visited.get(curNode, False): return

    visited[curNode] = True
    nextNodeList = nodeNext[curNode]
    for edge in nextNodeList:
        toNode, sym1, sym2 = edge
        curPath.append((toNode, sym1, sym2))
        findLambdaLoops(toNode, curPath)
        curPath.pop()

    visited[curNode] = False


findLambdaLoops("Lambda", [])  # ищем пути из вершины Lambda
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
        print('    Lambda', '\n')
        binStr = ""
        decode1 = ""
        decode2 = ""
        n = 1
        for edge in loop:
            print(' ->', edge[0], '\n')
            if edge[0] == "Lambda":
                binStr += edge[1]
            else:
                binStr += edge[1] + edge[0]
            decode1 = decode1 + getSymByCode(edge[n])
            decode2 = decode2 + getSymByCode(edge[3 - n])
            n = 3 - n
        print(": " + binStr, "=>", decode1, "=", decode2)
else:
    print('Циклов не обнаружено.')