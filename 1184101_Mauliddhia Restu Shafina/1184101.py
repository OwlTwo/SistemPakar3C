
#%%

#Foward Chain
global facts
global is_changed

is_changed = True
facts = [["monokotil","nanas"],["buah","nanas"],["dikotil","kentang"]]

def assert_fact(fact):
    global facts
    global is_changed
    if not fact in facts:
        facts += [fact]
        is_changed = True

while is_changed:
    is_changed = False
    for A1 in facts:
        if A1[0] == "buah":
            assert_fact(["monokotil",A1[1]])
        if A1[0] == "dikotil":
            assert_fact(["sayur",A1[1]])
        if A1[0] == "monokotil" and ["buah",A1[1]] in facts:
            assert_fact(["manis",A1[1]])

print("FowardChain")
print(facts)
#%%

#Backward Chain


is_changed = True
facts = [["monokotil","nanas"],["buah","nanas"],["dikotil","kentang"]]

def assert_fact(fact):
    global facts
    global is_changed
    if not fact in facts:
        facts += [fact]
        is_changed = True

while is_changed:
    is_changed = False
    for A1 in facts:
        if A1[0] == "monokotil" and ["buah",A1[1]] in facts:
            assert_fact(["manis",A1[1]])
        if A1[0] == "dikotil":
            assert_fact(["sayur",A1[1]])
        if A1[0] == "monokotil":
            assert_fact(["buah",A1[1]])
        
print("BackwardChain")
print(facts)