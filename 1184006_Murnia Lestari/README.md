# kecerdasanbuatan
Modul Praktikum Kecerdasan Buatan
Nama : Murnia Lestari
NPM : 114006
Kelas : D4 TI 3C
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 06:18:47 2021

@author: ACER
"""

#%%Contoh 1 Forward Chaining



# Terdapat Aturan dan Fakta  , disini kita akan mencari tanaman yang dapat dimakan oleh manusia dengan cara mengklasifikasikan beberapa tanaman aturannya seperti dibawah ini :
#plant ==> seed
#plant ==> eating
#plant,eating ==> manggo
#fakta :
#plant("manggo")
#eating("manggo")
#seed("sprouts")

#Forward Chaining merupakan algortima yang akan mengklasifikasikan data dengan fakta yang ada sehingga didapatkan kesimpulan
global is_changed
#mendefinisikan variable global is_changed

is_changed = True
# is_changed bernilai true
facts = [["plant","mango"],["eating","mango"],["seed","sprouts"]]
# fakta yang terjadi [["plant","mango"],["eating","mango"],["seed","sprouts"]]
def assert_fact(fact):
    #mendefiniskan class assert_fact(fact)
    global facts
    #mendefinisikan variable facts secara global
    global is_changed
    #mendefiniskan variable is_changed secara global
    if not fact in facts:
        #untuk menilai apakah rules yang didefinisikan pada facts merupakan sebuah fakta.
        facts += [fact]
        #jika fakta maka hasilnya akan + atau = fakta yang ada
        is_changed = True
        # fakta tersebut akan bernilai true

while is_changed:
    #bentuk perulangan dari is_changed
    is_changed = False
    # jika is_changed bernilai false
    for A1 in facts:
        # melalakukan perulangan pada variable A1 didalam fakta
        if A1[0] == "seed":
            #jika A1 merupakan seed
            assert_fact(["plant",A1[1]])
           # maka hasilnya seed tersebut merupakan tanaman
        if A1[0] == "plant":
            #jika A1 merupakan plant
            assert_fact(["fruit",A1[1]])
            #maka hasilnya plant tersebut merupakan buahan atau fruit
        if A1[0] == "plant" and ["eating",A1[1]] in facts:
            #jika A1 merupakan tanaman dan dimakan
            assert_fact(["human",A1[1]])
            #maka tanaman dan dimakan oleh manusia

print(facts)
#mencetak fakta yang ada
#%% Contoh 2 Backward Chaining

#Terdapat tanaman  ,kita akan mencari tanaman yang dapat dimakan oleh manusia dengan cara mengklasifikasikan beberapa tanaman aturannya seperti dibawah ini :
#plant ==> seed
#plant ==> eating
#plant,eating ==> manggo
#fakta
#plant("manggo")
#eating("manggo")
#seed("sprouts")
# Backward Chaining merupakan algoritma yang akan dimulai dari tujuan adanya pemcarian dengan data yang ada  sehingga didapatkan kesimpulan


global is_changed
#mendefinisikan variable global is_changed

is_changed = True
# is_changed bernilai true
facts = [["plant","mango"],["eating","mango"],["seed","sprouts"]]
# fakta yang terjadi [["plant","mango"],["eating","mango"],["seed","sprouts"]]
def assert_fact(fact):
    #mendefiniskan class assert_fact(fact)
    global facts
    #mendefinisikan variable facts secara global
    global is_changed
    #mendefiniskan variable is_changed secara global
    if not fact in facts:
        #untuk menilai apakah rules yang didefinisikan pada facts merupakan sebuah fakta.
        facts += [fact]
        #jika fakta maka hasilnya akan + atau = fakta yang ada
        is_changed = True
        # fakta tersebut akan bernilai true

while is_changed:
    #bentuk perulangan dari is_changed
    is_changed = False
    # jika is_changed bernilai false
    for A1 in facts:
        # melalakukan perulangan pada variable A1 didalam fakta
        if A1[0] == "plant" and ["eating",A1[1]] in facts:
            #jika A1 merupakan tanaman dan dimakan
            assert_fact(["human",A1[1]])
            #maka tanaman dan dimakan oleh manusia
        if A1[0] == "seed":
            #jika A1 merupakan seed
            assert_fact(["plant",A1[1]])
           # maka hasilnya seed tersebut merupakan tanaman
        if A1[0] == "plant":
            #jika A1 merupakan plant
            assert_fact(["fruit",A1[1]])
            #maka hasilnya plant tersebut merupakan buahan atau fruit
       

print(facts)
#mencetak fakta yang ada
#%% Contoh 3
# Contoh dibawah ini akan memprediksi value atau nilai yang akan kita inputkan berdasarkan dengan fakta yang tersedia
# Apabila apa yang kita inputkan tidak sesuai dengan fakta yang ada maka sistem akan merespon dengan "Haram Command" artinya
# sistem ini akan memprediksi inputan dari pengguna sesuai dengan faka yang ada pada sistem ini .
# C dan D bernilai true
# A + B = C
# D + E = F
# F = G
# C = H





from collections import OrderedDict
# dari library collection mengimport OrderedDict

class Variable:
   # mendefinisikan class 
    def __init__(self, value, truth, root):
        # mendefinsiikan fungsi
        self.value = value
        self.truth = truth
        self.root = root
        # untuk memanggil sebuah variable pada fungsi diatas
    def get_value(self):
        # mendefinisikan fungsi
        return self.value
    #mengembalikan nilai
    
    def get_truth(self):
        # mendefinisikan fungsi
        return self.truth
    # untuk mengembalikan nilai
    
    def get_root(self):
# mendefinisikan fungsi
        return self.root
# untuk mengembalikan nilai
    
    def set_truth(self, truth):
# mendefinisikan fungsi
        self.truth = truth
# untuk mengembalikan nilai
    
    def __str__(self):
#mendefinisikan fungsi
        return "{ value = " + self.value + ", truth = " + str(self.truth) + ", root = " + str(self.root) + " }"
    #mengembalikan nilai
    def __repr__(self):
#mendefinisikan fungsi
        return str(self)
    #mengembalikan nilai
class Rule:
#mendefinisikan kelas
    
    def __init__(self, antecedent, consequent):
#mendefinisikan fungsi
        self.antecedent = antecedent
#untuk memanggil sebuah variable diatas
        self.consequent = consequent
#untuk memanggil sebuah variabel diatas
    def get_antecedent(self):
#untuk mendefinisikan fungsi
        return self.antecedent
    #untuk mengembalikan nilai
    def get_consequent(self):
#untuk mendefinisikan fungsi 
        return self.consequent
#untuk mengembalikan nilai
    
    def __str__(self):
    #untuk mendefinisikan fungsi
        return str(self.antecedent) + " -> " + str(self.consequent)
# untuk mengembalikan nilai
    def __repr__(self):
#untuk mendefinisikan fungsi
        return str(self)
# untuk mengembalikan nilai
    
    
def valid_rule(antecedent, consequent, variables):
    #untukmendefinisikan rule
    antecedent = antecedent.replace("(", " ( ")
    antecedent = antecedent.replace(")", " ) ")
    antecedent = antecedent.replace("&", " AND ")
    antecedent = antecedent.replace("|", " OR ")
    antecedent = antecedent.replace("!", " NOT ")
    antecedent = antecedent.split()
    
    for a in antecedent:
# untuk melakukan perualngan pada antecedent
        if a not in ["(", ")", "AND", "OR", "NOT"]:
# jika tidak dalam antecedent variable
            if a not in variables:
#jika tidak didalam variable diatas
                return False
#maka mengembalikan nilai else
    
    if consequent not in variables or variables[consequent].get_root():
#jika konsequen tidak didalam variable atau variable consequent memanggil fungsi get_root
        return False
#mengembalikan nilai false
    
    return True
#mengembalikan nilai true

def reset_learned(variables): 
#mendefinisikan fungsi
    
    for key in variables:
#melakukan perulangan pada variable
        if not variables[key].get_root():
            variables[key].set_truth(False)
    
def is_fact(var, variables):
#mendefinisikan fakta apabila  variabel di variabel get_truth maka akan mengembalikan nilai true jika tidka maka false
    
    if var in variables and variables[var].get_truth():
        return True
    else:
        return False
    
def format_rule(antecedent, consequent, variables, rules):
    #mendefinisikan fungsi serta memvalidtasi data dengan antecedent yang ada
    valid = query_exp(consequent, variables, rules)
    
    antecedent = antecedent.replace("(", " ( ")
    antecedent = antecedent.replace(")", " ) ")
    antecedent = antecedent.replace("&", " AND ")
    antecedent = antecedent.replace("|", " OR ")
    antecedent = antecedent.replace("!", " NOT ")
    
    antecedent = antecedent.split()
    
    for i in range(len(antecedent)):
#lalu melakukan perulangan
        if antecedent[i] not in ["(", ")", "AND", "OR", "NOT"]:
            antecedent[i] = variables[antecedent[i]].get_value()
            
    if antecedent[0] == "NOT":
        new_ant = str(antecedent[0]) + " "
    else:
        new_ant = str(antecedent[0])
    
    for a in range(1, len(antecedent)):
        if antecedent[a] in ["AND", "OR"]:
            new_ant += " " + str(antecedent[a]) + " "
        elif antecedent[a] == "NOT":
            new_ant += str(antecedent[a]) + " "
        else:
            new_ant += str(antecedent[a])
            
    antecedent = new_ant
    
    if valid:
#jika valid maka sistem akan mengembalikan nilai baik 
        return "BECAUSE " + antecedent + " I KNOW THAT " + variables[consequent].get_value()
    else:
        return "BECAUSE IT IS NOT TRUE THAT " + antecedent + " I CANNOT PROVE THAT " + variables[consequent].get_value()

def format_goal(goal, variables):
#mendefinisikan fungsi
    
    goal = goal.replace("(", " ( ")
    goal = goal.replace(")", " ) ")
    goal = goal.replace("&", " AND ")
    goal = goal.replace("|", " OR ")
    goal = goal.replace("!", " NOT ")
    
    goal = goal.split()
    
    for i in range(len(goal)):
        if goal[i] not in ["(", ")", "AND", "OR", "NOT"]:
            goal[i] = variables[goal[i]].get_value()
            
    if goal[0] == "NOT":
        new_goal = str(goal[0]) + " "
    else:
        new_goal = str(goal[0])
    
    for g in range(1, len(goal)):
        if goal[g] in ["AND", "OR"]:
            new_goal += " " + str(goal[g]) + " "
        elif goal[g] == "NOT":
            new_goal += str(goal[g]) + " "
        else:
            new_goal += str(goal[g])
            
    return new_goal
       
def solve(expression, variables):
    
    expression = expression.replace('(', '( ')
    expression = expression.replace(')', ' )')
    expression = expression.replace('&', ' and ')
    expression = expression.replace('|', ' or ')
    expression = expression.replace('!', 'not ')
    
    expression_list = expression.split()
    
    for i in range(len(expression_list)):

        if expression_list[i] not in ['not', 'or', 'and', '(', ')']:
            expression_list[i] = variables[expression_list[i]].get_truth()
            
    expression = str(expression_list[0]) + " "

    for i in range(1, len(expression_list)):
        expression += str(expression_list[i]) + " "
        
    return eval(expression)

def query_exp(expression, variables, rules, why=False):
    #mendefinisikan fungsi
    expression = expression.replace('(', '( ')
    expression = expression.replace(')', ' )')
    expression = expression.replace('&', ' and ')
    expression = expression.replace('|', ' or ')
    expression = expression.replace('!', 'not ')
    
    expression_list = expression.split()
    #melakukan perulangan
    for i in range(len(expression_list)):
        if expression_list[i] not in ['not', 'or', 'and', '(', ')']:
            
            found = False
            
            for rule in rules:
                
                if rule.get_consequent() == expression_list[i]:
                    found = True
                    expression_list[i] = query_exp(rule.get_antecedent(), variables, rules)
                    
            if not found:
                expression_list[i] = variables[expression_list[i]].get_truth()
                        
    expression = str(expression_list[0]) + " "

    for i in range(1, len(expression_list)):
        expression += str(expression_list[i]) + " "
        
    return eval(expression)   

def why_exp(expression, variables, rules, start=False):
   #mendefinsikan fungsi 
    result = list()
    #hasil akan berupa list
    if start and query_exp(expression, variables, rules):
        reasoning = "I THUS KNOW THAT "
    elif start:
        reasoning = "THUS I CANNOT PROVE "
        
    temp = expression.replace('(', '( ')
    temp = temp.replace(')', ' )')
    temp = temp.replace('&', ' and ')
    temp = temp.replace('|', ' or ')
    temp = temp.replace('!', 'not ')
    
    exp_list = temp.split()
    
    print(exp_list)
        #mencetak hasil
    for i in range(len(exp_list)):
        if exp_list[i] not in ['&', '|', '!', '(', ')']:
            exp_list[i] = variables[exp_list[i]].get_value()
            
    for x in exp_list:
        reasoning += str(x)
    
    reasoning = reasoning.replace('(', ' ( ')
    reasoning = reasoning.replace(')', ' ) ')
    reasoning = reasoning.replace('&', ' AND ')
    reasoning = reasoning.replace('|', ' OR ')
    reasoning = reasoning.replace('!', ' NOT ')
    
    result.append(reasoning)
    
    count = 0
    addition, count = simplify(expression, variables, rules, count)
    
    result.extend(addition)
    
    return result, count

def determine_why(expression, variables, rules):
  #mendefinisikan fungsi  
    valid = query_exp(expression, variables, rules)
    
    logic = list()
        
    logic.append(expression)
        
    done = False
        
    expression = expression.replace('(', ' ( ')
    expression = expression.replace(')', ' ) ')
    expression = expression.replace('&', ' & ')
    expression = expression.replace('|', ' | ')
    expression = expression.replace('!', ' ! ')
            
    exp_list = expression.split()
        
    while not done:
#perulangan jika tidak selesai
            
        done = True
        change = False
            
        for i in range(len(exp_list)):
#melakukan perulangan dalam range
            if exp_list[i] not in ['!', '|', '&', '(', ')'] and not variables[exp_list[i]].get_truth():
                for rule in rules:
                    if rule.get_consequent() == exp_list[i]:
                            
                        exp_list[i] = rule.get_antecedent()
                            
                        exp_list[i] = exp_list[i].replace('(', ' ( ')
                        exp_list[i] = exp_list[i].replace(')', ' ) ')
                        exp_list[i] = exp_list[i].replace('&', ' & ')
                        exp_list[i] = exp_list[i].replace('|', ' | ')
                        exp_list[i] = exp_list[i].replace('!', ' ! ')
                        
                        exp_list[i] = exp_list[i].split()
                            
                        exp_list = exp_list[:i] + exp_list[i] + exp_list[i+1:]
                        done = False
                        change = True
                        break
            if change:
                
                str_exp = str(exp_list[0])
                
                for i in range(1, len(exp_list)):
                    str_exp += str(exp_list[i])
                
                logic.append(str_exp)
                change = False
            
    return valid, logic


def get_diff(a, b):
#mendefinsikan fungsi
    
    unique = ""
    
    a = a.replace('(', ' ( ')
    a = a.replace(')', ' ) ')
    a = a.replace('&', ' & ')
    a = a.replace('|', ' | ')
    a = a.replace('!', ' ! ')
        
    a = a.split()
    
    for i in a:
        if i not in b and i not in ['!', '|', '&', '(', ')']:
            unique = i
            
    return unique

if __name__ == "__main__":
    
    print("\n\t\tHello! I'm Halal-bot, and I'm smarter than you.", end='\n\n')
    
    var_list = OrderedDict()
    rule_list = list()
     #melakukan perulangan nilai
    while True:
        
        teach_var = False
        set_root = False
        teach_rule = False
        list_knowledge = False
        learn = False
        query = False
        why = False
        index = None
    
        user_input = input("Enter a new definition, fact, or rule: ").split('"')
        
        if user_input[0] == '':
            break
        
        args = user_input[0].split()
        
        if len(user_input) > 1:
            
            args.append(user_input[1])
            
            if len(args) != 5:
                continue
            
            teach_var = True
        
        if len(args) == 1:
            if args[0] == 'List':
                list_knowledge = True
            if args[0] == 'Learn':
                learn = True
                
        if len(args) == 2:
            if args[0] == 'Query':
                query = True
            if args[0] == 'Why':
                why = True
            
            
        if not teach_var:
            
            for i in range(len(args)):
                if args[i] == '=':
                    set_root = True
                    index = i
                if args[i] == '->':
                    teach_rule = True
                    index = i
        
        if teach_var:
            
            var_defined = False
            
            for key in var_list:
                if key == args[2]:
                    print("\nVariable already defined.")
                    var_defined = True
                    
            if var_defined:
                continue
            
            if args[1] == '-R':
                var_list[args[2]] = Variable(args[4], False, True)
            else:
                var_list[args[2]] = Variable(args[4], False, False)
                
        elif set_root:
            
            if args[1] not in var_list:
                print("\nVariable not defined.")
                continue
            
            if var_list[args[1]].get_root():
                if args[3] == 'true':
                    var_list[args[1]].set_truth(True)
                    reset_learned(var_list)
                elif args[3] == 'false':
                    var_list[args[1]].set_truth(False)
                    reset_learned(var_list)
                else:
                    print("\nInvalid assignment. Assign 'true' or 'false.'")
            else:
                print("\n" + str(args[1]) + " is not a root variable.")
            
        elif teach_rule:
            
            antecedent = args[1]
            consequent = args[-1]
            
            if valid_rule(antecedent, consequent, var_list):
                rule_list.append(Rule(antecedent, consequent))
            else:
                continue
            
        elif list_knowledge:
            
            print("\nRoot Variables:")
            for key in var_list:
                if var_list[key].get_root():
                    print("\t" + key + " = " + '"' + var_list[key].get_value() + '"')
            print("\nLearned Variables:")
            for key in var_list:
                if not var_list[key].get_root():
                    print("\t" + key + " = " + '"' + var_list[key].get_value() + '"')
            print("\nFacts:")
            for key in var_list:
                if var_list[key].get_truth():
                    print("\t" + key)
            print("\nRules:")
            for rule in rule_list:
                print("\t" + rule.__str__())
        
        elif learn:
            
            for rule in rule_list:
                if solve(rule.get_antecedent(), var_list):
                    var_list[rule.get_consequent()].set_truth(True)
                else:
                    var_list[rule.get_consequent()].set_truth(False)
           

        elif query:
            
            print("\n" + str(query_exp(args[1], var_list, rule_list)))
            
        elif why: 
            
            valid, logic = determine_why(args[1], var_list, rule_list)
                            
            print("\n" + str(valid))
            
            fact_list = list()
            
            for step in logic:
                
                step = step.replace("(", " ( ")
                step = step.replace(")", " ) ")
                step = step.replace("&", " & ")
                step = step.replace("|", " | ")
                step = step.replace("!", " ! ")
                
                step = step.split()
                
                for i in step:
                    if i not in ["(", ")", "&", "|", "!"] and i not in fact_list and var_list[i].get_root():
                        fact_list.append(i)
                
            for fact in fact_list:
                
                if var_list[fact].get_truth():
                    print("I KNOW THAT " + var_list[fact].get_value())
                else:
                    print("I KNOW IT IS NOT TRUE THAT " + var_list[fact].get_value())
                
            i = len(logic)-1
             
            while i >= 0:
                
                if i > 0:
                
                    con = get_diff(logic[-2], logic[-1])
                    ant = ""
                    
                    for rule in rule_list:
                        if rule.get_consequent() == con:
                            ant = rule.get_antecedent()
                            
                    print(format_rule(ant, con, var_list, rule_list))
                            
                else:
                    
                    if valid:
                        print("I THUS KNOW THAT", format_goal(logic[0], var_list))
                    else:
                        print("THUS I CANNOT PROVE", format_goal(logic[0], var_list))
                
                i -= 1
                logic.pop()        
            
        else:
            print("\nHaram Command.")
    
        print()
        
