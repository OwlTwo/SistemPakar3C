#%Contoh 1 Forward Chaining

global facts
global is_changed

is_changed = True
facts = [["drum","dipukul"],["gendang","dipukul"],["bass","dibetot"]]

def assert_fact(fact):
	global facts
	global is_changed
	if not fact in facts:
		facts += [fact]
		is_changed = True

while is_changed:
	is_changed = False
	for A1 in facts:
		if A1[0] == "bass":
			assert_fact(["dibetot",A1[1]])
		if A1[0] == "drum":
			assert_fact(["pukul",A1[1]])
		if A1[0] == "drum" and ["gendang",A1[1]] in facts:
			assert_fact(["alat musik",A1[1]])

print(facts)

is_changed = True
facts = [["drum","dipukul"],["gendang","dipukul"],["bass","dibetot"]]

def assert_fact(fact):
    global facts
    global is_changed
    if not fact in facts:
        facts += [fact]
        is_changed = True

while is_changed:
    is_changed = False
    for A1 in facts:
        if A1[0] == "drum" and ["gendang",A1[1]] in facts:
            assert_fact(["alat musik",A1[1]])
        if A1[0] == "drum":
            assert_fact(["pukul",A1[1]])
        if A1[0] == "bass":
            assert_fact(["dibetot",A1[1]])

print("BackwardChain")
print(facts)