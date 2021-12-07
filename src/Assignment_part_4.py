import utils
from logic import *


clauses = [expr("Women(Jia)"), expr("Man(John)"),
           expr("Healthy(John)"), expr("Healthy(Jia)"),
           expr("Wealthy(John)"), 
           expr("(Wealthy(x) & Healthy(x)) ==> Traveler(x)")]

KB = FolKB(clauses)
wealthy = fol_fc_ask(KB, expr("Wealthy(x)"))
healthy = fol_fc_ask(KB, expr("Healthy(x)"))
traveler = fol_fc_ask(KB, expr("Traveler(x)"))
print('Who are healthy ?')
print(list(healthy))
print('\n Who are wealthy ?')
print(list(wealthy))
print('\n Who can travel ?')
print(list(traveler))
