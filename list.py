
#list-append

a=["bee","moth"]
print(a)                     # ['bee', 'moth']
a.append("ant")
print(a)                    # ['bee', 'moth', 'ant']
a.append("siri")
a.append("mango")
print(a)                    # ['bee', 'moth', 'ant', 'siri', 'mango']


#list-extend

a=["bee","moth"]
print(a)                    # ['bee', 'moth']
a.extend(["ant","fly"])
print(a)                    # ['bee', 'moth', 'ant', 'fly']


#list-insert

a=["bee","moth"]
print(a)                    # ['bee', 'moth']
a.insert(0,"ant")
print(a)                    # ['ant', 'bee', 'moth']
a.insert(1,"element")
print(a)                    # ['ant', 'element', 'bee', 'moth']


#list-remove

a=["siri","jyothi","bala","jojappa"]
print(a)                    # ['siri', 'jyothi', 'bala', 'jojappa']
a.remove("jyothi")          # ['siri', 'bala', 'jojappa']
print(a)


#list-pop

a=["bee","siri","ant"]
print(a)                    # ['bee', 'siri', 'ant']
a.pop(1)
print(a)                    # ['bee', 'ant']


#list-clear

a=["jyothi","siri","anthoni"]
print(a)                    # ['jyothi', 'siri', 'anthoni']
a.clear()
print(a)                    # []


#list-index

a=["bee","ant","tiger","lion"]
print(a)                    # ['bee', 'ant', 'tiger', 'lion']
print(a.index("ant"))       # 1
print(a)                    # ['bee', 'ant', 'tiger', 'lion']
print(a.index("ant",1))     # 1


#list-count

a=["bee","siri","ant","lion","ant"]
print(a.count("bee"))       # 1
print(a.count("ant"))       # 2
print(a.count("lion"))      # 1
print(a.count(" "))         # 0


#list-sort

a=[3,4,5,6,1,2,8]
a.sort()
print(a)                    # [1, 2, 3, 4, 5, 6, 8]
a=[3,6,5,2,4,1,7]
a.sort(reverse=True)
print(a)                    # [7, 6, 5, 4, 3, 2, 1]
a=["bee","wasp","moth","ant"]
a.reverse()
print(a)                    # ['ant', 'moth', 'wasp', 'bee']


#list-copy

a=["siri","anthoni","jyothi"]
b=a.copy()
b.append("jojappa")
print(a)                    # ['siri', 'anthoni', 'jyothi']
print(b)                    # ['siri', 'anthoni', 'jyothi', 'jojappa']
print(len(a))               # 3
print(len(b))               # 4



#list-iterable

print(list())                           # []
print(list([]))                         # []
print(list(["bee","moth","ant"]))       # ['bee', 'moth', 'ant']
print(list([["bee","moth"],["ant"]]))   # [['bee', 'moth'], ['ant']]


#list-max

a=["siri","jyothi","anthoni"]
print(max(a))               # siri
a=[3,2,5,4,7,9,1,6]
b=[2,4,6,5,3,1,9]
print(max(a,b))             # [3, 2, 5, 4, 7, 9, 1, 6]


#list-main

a=["siri","mama","teddy","dog"]
print(min(a))               # dog


#list-range

print(list(range(10)))      # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(1,11)))    # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(range(51,56)))   # [51, 52, 53, 54, 55]
print(list(range(1,11,2)))  # [1, 3, 5, 7, 9]