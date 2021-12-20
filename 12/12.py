kek = """
yw-MN
wn-XB
DG-dc
MN-wn
yw-DG
start-dc
start-ah
MN-start
fi-yw
XB-fi
wn-ah
MN-ah
MN-dc
end-yw
fi-end
th-fi
end-XB
dc-XB
yw-XN
wn-yw
dc-ah
MN-fi
wn-DG
""".split("\n")

kek.remove("")
kek.remove("")

graph = {}

for k in kek:
    fr = k.split("-")[0]
    to = k.split("-")[1]

    if not fr in graph:
        graph[fr] = [] 
    if not to in graph:
        graph[to] = [] 

    graph[fr].append(to)
    graph[to].append(fr)

graph["end"] = []
[graph[k].remove("start") for k in graph if "start" in graph[k]]

paths = []
def depthFirst(current_node, visited):
    visited.append(current_node)
    for n in graph[current_node]:
        if n not in visited or n.isupper(): #or ((not n.isupper()) and visited.count(n) <= 1 and not ([True for k in visited if (not k.isupper()) and visited.count(k) == 2])):
            depthFirst(n, visited.copy())        
    paths.append(visited)
depthFirst("start", [])

print(len([k for k in paths if k[-1] == "end"]))
