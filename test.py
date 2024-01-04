from state import next_state
import time


def addTograph(graph, final):
 empty = []
 # if node not in graph:
 #     graph[node] = []
 for n in graph:
  if graph[n] == []:
   empty.append(n)
   #m = n[:-1]
   li = [list(map(int, tpl)) for tpl in n]
   first = tuple(map(tuple, next_state(li, 1)))
   if first == final:
    print("Buldum")
    time.sleep(20)
   a = (1, 1)
   first = first + (a,)
   second = tuple(map(tuple, next_state(li, 6)))
   if second == final:
    print("Buldum")
    time.sleep(20)
   b = (2, 2)
   second = second + (b,)
   third = tuple(map(tuple, next_state(li, 2)))
   if third == final:
    print("Buldum")
    time.sleep(20)
   c = (3, 3)
   third = third + (c,)
   forth = tuple(map(tuple, next_state(li, 5)))
   if forth == final:
    print("Buldum")
    time.sleep(20)
   d = (4, 4)
   forth = forth + (d,)
   fifth = tuple(map(tuple, next_state(li, 3)))
   if fifth == final:
    print("Buldum")
    time.sleep(20)
   e = (5, 5)
   fifth = fifth + (e,)
   sixth = tuple(map(tuple, next_state(li, 4)))
   if sixth == final:
    print("Buldum")
    time.sleep(20)
   f = (6, 6)
   sixth = sixth + (f,)
   seventh = tuple(map(tuple, next_state(li, 7)))
   if seventh == final:
    print("Buldum")
    time.sleep(20)
   g = (7, 7)
   seventh = seventh + (g,)
   eighth = tuple(map(tuple, next_state(li, 12)))
   if eighth == final:
    print("Buldum")
    time.sleep(20)
   h = (8, 8)
   eighth = eighth + (h,)
   ninth = tuple(map(tuple, next_state(li, 8)))
   if ninth == final:
    print("Buldum")
    time.sleep(20)
   i = (9, 9)
   ninth = ninth + (i,)
   tents = tuple(map(tuple, next_state(li, 11)))
   if tents == final:
    print("Buldum")
    time.sleep(20)
   j = (10, 10)
   tents = tents + (j,)
   eleventh = tuple(map(tuple, next_state(li, 9)))
   if eleventh == final:
    print("Buldum")
    time.sleep(20)
   k = (11, 11)
   eleventh = eleventh + (k,)
   twleveth = tuple(map(tuple, next_state(li, 10)))
   if twleveth == final:
    print("Buldum")
    time.sleep(20)
   l = (12, 12)
   twleveth = twleveth + (l,)
 for n in empty:
  if first not in graph:
   graph[first] = []
   graph[n].append(first)
   return graph
  if second not in graph:
   graph[second] = []
   graph[n].append(second)
   return graph
  if third not in graph:
   graph[third] = []
   graph[n].append(third)
   return graph
  if forth not in graph:
   graph[forth] = []
   graph[n].append(third)
   return graph
  if fifth not in graph:
   graph[fifth] = []
   graph[n].append(fifth)
   return graph
  if sixth not in graph:
   graph[sixth] = []
   graph[n].append(sixth)
   return graph
  if seventh not in graph:
   graph[seventh] = []
   graph[n].append(seventh)
   return graph
  if eighth not in graph:
   graph[eighth] = []
   graph[n].append(first)
   return graph
  if ninth not in graph:
   graph[ninth] = []
   graph[n].append(ninth)
   return graph
  if tents not in graph:
   graph[tents] = []
   graph[n].append(tents)
   return graph
  if eleventh not in graph:
   graph[eleventh] = []
   graph[n].append(eleventh)
   return graph
  if twleveth not in graph:
   graph[twleveth] = []
   graph[n].append(twleveth)
   return graph

  return None

g = {}

st = (
 (2, 2),
 (6 ,4),
 (6 ,3),
 (3 ,4),
 (2 ,3),
 (3 ,4),
 (6 ,1),
 (5 ,1),
 (5 ,5),
 (5 ,1),
 (1 ,6),
 (2 ,4)
)

f = (
 (1, 1),
 (1 ,1),
 (2 ,2),
 (2 ,2),
 (3 ,3),
 (3 ,3),
 (4 ,4),
 (4 ,4),
 (5 ,5),
 (5 ,5),
 (6 ,6),
 (6 ,6)
)

g[st] = []

# while True:
#  addTograph(g, f)

li = [1,2]
li1 = [1]

if li[:-1] == li1:
   print("233333")
print(li)