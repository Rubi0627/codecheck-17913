N = int(sys.stdin.readline())

M = []
for i in range(N):
    inp = sys.stdin.readline()
    inp = inp.rstrip()
    M.append(inp)

for m in M:
    e = m.split(" ")
    print(repr(e))
    
    for s in e:
        print(s)