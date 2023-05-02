import random
import sys

# Function to convert input fle into graph
def file_extract(path1):
    # Reading files
    file = open(path1, mode = 'r')
    graph = file.readlines()
    file.close()
    # Extracting edges and vertices
    all_edge = []
    all_vertices = set()
    for ed in graph:
        ed = ed.split()
        item = [int(ed[0]), int(ed[1])]
        item.sort()
        all_edge.append(item)
        all_vertices.add(item[0])
        all_vertices.add(item[1])
    return all_edge, all_vertices

# Function to find min_cut value
def min_cut(edge):
    # Stores edges chose for merging
    sel_edge = []
    while 1:
        # Stoping condition if only 1 edge left
        # Random selection of edge
        cur_edge = random.choice(edge)
        sel_edge.append(cur_edge)
        # Removing selected edge from graph
        edge = [rem for rem in edge if rem != cur_edge]
        # Replacing second node of selected edge with first
        for i in range(len(edge)):
            if edge[i][0] == cur_edge[1]:
                edge[i][0] = cur_edge[0]
            elif edge[i][1] == cur_edge[1]:
                edge[i][1] = cur_edge[0]
                edge[i].sort()
        # Checking for stopping condition
        if len(edge) == 1:
            return sel_edge, len(edge)
            break
        for i in edge[1:]:
            if edge[0] != i:
                n = 1
                break
            else:
                n = 0
        if n == 0: break
    return sel_edge, len(edge)

# Function to find communities formed
def community(opt_cut):
    com = set(opt_cut[0])
    # Identifying community with same edges
    while 1:
        n = 1
        for i in opt_cut[1:]:
            if i[0] in com:
                com.add(i[1])
                opt_cut.remove(i)
                n = 0
            elif i[1] in com:
                com.add(i[0])
                opt_cut.remove(i)
                n = 0
        if n == 1: break
    return com

# Input path of input file
path1 = sys.argv[1]

# Constructing graph
all_edge, all_vertices = file_extract(path1)

# Computing minimum cut and merged edges
opt_cut, cuts = min_cut(all_edge)

# Finding Communities
com1 = community(opt_cut)
com2 = all_vertices - com1

# Printing final output
out = []
for i in com1:
    out.append(' '.join([str(i), str(1)]))
for i in com2:
    out.append(' '.join([str(i), str(2)]))

for i in out:
    print(i)
print("Minimum Cut value is: ", cuts)
