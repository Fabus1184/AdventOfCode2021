import networkx as nx
import time
    
def do(kek, l):
    kek = [int(k) for k in kek]

    g = nx.MultiDiGraph()
    [g.add_node((x,y)) for x in range(l) for y in range(l)]
    for i in range(len(kek)):
        if i % l != l - 1:
            g.add_edge((i // l, i % l), (i // l, i % l+1), weight=kek[i+1])
        if i % l != 0:
            g.add_edge((i // l, i % l), (i // l, i % l-1), weight=kek[i-1])
        if i // l != 0:
            g.add_edge((i // l, i % l), (i // l-1, i % l), weight=kek[i-l])
        if i // l != l - 1:
            g.add_edge((i // l, i % l), (i // l+1, i % l), weight=kek[i+l]) 

    print(str(g) + "\nCompute A*")
    path = nx.astar_path(g, (0,0), (l-1, l-1))
    print(nx.path_weight(g, path, "weight"))
    return (g, path)

def a1():
    from input_fuenfzehn import kek
    do(kek, 100)

def a2():
    from input_fuenfzehn import kek2
    (graph, path) = do(kek2, 500)
#    plot(graph, path)

def plot(g, path):
    from input_fuenfzehn import test
    colors = ["lightblue" if n in path else "lightgreen" for n in g.nodes()]
    pos = {(x,y) : (y, -x) for x,y in g.nodes() if (x,y)}
    nx.draw_networkx_nodes(g, pos, node_color=colors)
    labels = {k[0][:2]: k[1]["weight"] for k in g.edges.items()}
    nx.draw_networkx_edges(g, pos, connectionstyle="arc3, rad=0.2")
    nx.draw_networkx_edge_labels(g, pos, edge_labels=labels, rotate=False, label_pos=0.25, font_size=10, font_color="orange", alpha=1.0, font_weight="bold", bbox=dict(alpha=0))
    plt.savefig("15.png", dpi=1000)

#a1()
a2()
