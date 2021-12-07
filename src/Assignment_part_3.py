from utils import *
from logic2 import *

#**************************
# 1

x = Symbol("x")
y = Symbol("y")
enemies = Symbol("enemies(x, y)")
hates1 = Symbol("hates(x, y)")
hates2 = Symbol("hates(y, x)")
knowledge_num1 = And(Implication(enemies, And(hates1, hates2)))
print(knowledge_num1.formula())

#**************************
# 2

p = Symbol("p(x)")
q = Symbol("q(x)")
r = Symbol("r(x)")
knowledge_num2 = And(Implication(p , And(q, r)))
print(knowledge_num2.formula())
