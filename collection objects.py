#collections:Counter, namedtuple, OrderedDict, defaultdict, deque
#Counter
from collections import Counter
a="aaaaabbbbcccc"
my_counter= Counter(a)
print(my_counter)
print(my_counter.items())
print(my_counter.keys())
print(my_counter.values())
print(my_counter.most_common(1)[0][0])
print(list(my_counter.elements()))
#namedtuples
from collections import namedtuple
Point= namedtuple('Point', 'x,y')
pt=Point(1,-4)
print(pt.x, pt.y)
#OrderedDict, Remembers the order of key value pairs inserted
from collections import OrderedDict
ordered_dict= OrderedDict()
ordered_dict['a']=1
ordered_dict['b']=2
ordered_dict['c']=3
ordered_dict['d']=4
print(ordered_dict)
#defaultdict
from collections import defaultdict
d= defaultdict(int)
d['a']=1
d['b']=2
print(d['c'])#returns the default value of the type specified as an argument in the defaultdict function above
#deque
from collections import deque
d=deque()
d.append(1)
d.append(2)
print(d)
d.appendleft(3)
print(d)
d.extend([4,5,6])
print(d)
d.extendleft([7,8])
print(d)
d.pop()
print(d)
d.popleft()
print(d)
d.rotate(1)#positive numbers rotate the elements to the right, where negative elements rotate the elements to the left
print(d)
d.rotate(-3)
print(d)
d.clear()
print(d)