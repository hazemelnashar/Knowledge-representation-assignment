from utils import *
from logic2 import *

#************************
# 1

maria = Symbol("maria")
reads = Symbol(" reads (maria, logic programming book)")
by = Symbol("by author (peter_lucas)")
knowledge_num1 = And(Implication(reads, by))
print(knowledge_num1.formula())
 
#************************
# 2

is_girl = Symbol("is_girl(x)")
shopping = Symbol("shopping")
like = Symbol("like(x, shopping)")
knowledge_num2 = And(Implication(is_girl, like))
print(knowledge_num2.formula())

#*************************
# 3

who = Symbol("?")
# like = Symbol("like(x, shopping)")
knowledge_num3 = And(who, like)
print(knowledge_num3.formula())

#*************************
# 4

city = Symbol("city(x, big, crowdy)")
hates = Symbol("hates(kirke, x)")
knowledge_num4 = And(Implication(city, hates))
print(knowledge_num4.formula())
