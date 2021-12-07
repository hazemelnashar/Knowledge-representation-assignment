from logic2 import *

#*************************
# 1

carrots = Symbol("carrots")
orange = Symbol("orange")
knowledge_num1 = And(
    Implication(carrots, orange))
print("Carrots color is Orange.")
print(knowledge_one.formula()) 

#*************************
# 2

person = Symbol("person(x)")
like = Symbol("like")
vegetarian = Symbol("vegetarian(x)")
like_person_carrots = Symbol("like(x, carrots)")
knowledge_num2 = And(Implication(vegetarian, like_person_carrots))
print("if person is vegetarian, person likes carrots.")
print(knowledge_num2.formula())

#*************************
# 3

Pass = Symbol("pass(x)")
study_hard = Symbol("study_hard(x)")
knowledge_num3 = Implication(study_hard, Pass)
print("if student study hard, student pass.")
print(knowledge_num3.formula())

#*************************
# 4

Pass = Symbol("?-pass(who)")
knowledge_num4 = And(Pass)
print("who will pass?")
print(knowledge_num4.formula())

#*************************
# 5

teaches = Symbol("?-teaches(professor ,Course)")
knowledge_num5 = And(teaches)
print("which course professor teaches?")
print(knowledge_num5.formula())

#*************************
# 6

x = Symbol("x")
y = Symbol("y")
enemies = Symbol("enemies(x, y)")
hates = Symbol("hates(x, y)")
fight = Symbol("fight(x, y)")
knowledge_num6 = And(Implication(And(hates, fight) ,enemies))
print("if x hates y and x fights y, x & y are enemies.")
print(knowledge_num6.formula())
