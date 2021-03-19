#%%Contoh 1 Forward Chaining

global facts
global is_changed

is_changed = True
facts = [["saxophone","ditiup"],["harmonika","ditiup"],["biola","digesek"]]

def assert_fact(fact):
	global facts
	global is_changed
	if not fact in facts:
		facts += [fact]
		is_changed = True

while is_changed:
	is_changed = False
	for A1 in facts:
		if A1[0] == "biola":
			assert_fact(["digesek",A1[1]])
		if A1[0] == "saxophone":
			assert_fact(["tiup",A1[1]])
		if A1[0] == "saxophone" and ["harmonika",A1[1]] in facts:
			assert_fact(["alat musik",A1[1]])

print(facts)
#%%Contoh 2 backward Chaining
is_changed = True
facts = [["saxophone","ditiup"],["harmonika","ditiup"],["biola","digesek"]]

def assert_fact(fact):
    global facts
    global is_changed
    if not fact in facts:
        facts += [fact]
        is_changed = True

while is_changed:
    is_changed = False
    for A1 in facts:
        if A1[0] == "saxophone" and ["harmonika",A1[1]] in facts:
            assert_fact(["alat musik",A1[1]])
        if A1[0] == "saxophone":
            assert_fact(["tiup",A1[1]])
        if A1[0] == "biola":
            assert_fact(["digesek",A1[1]])

print("BackwardChain")
print(facts)