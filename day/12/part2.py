class Node:
    def __init__(self, name, path=[], visits={}, doubled=False):
        self.name = name
        self.children = []
        self.path = path + [self.name]
        self.visits = {}
        self.visits.update(visits)
        self.doubled = doubled
        if self.name[0].islower() and self.name in self.visits:
            if self.doubled:
                print("visits", self.visits, "name:", self.name)
                raise ValueError
            else:
                self.doubled = True
        else:
            self.visits[self.name] = True    

    def __str__(self):
        return """Node: {}
        children: {}""".format(self.name, self.children)

def build_tree(graph):
    root = Node("start")
    for c in graph["start"]:
        root.children.append(Node(c, root.path))
    queue = root.children[:]
    while queue:
        cur = queue.pop(0)
        for c in graph.get(cur.name, []):
            if c[0].isupper() or c not in cur.path:
                cur.children.append(Node(c, cur.path, cur.visits, cur.doubled))
            elif c[0].islower() and c not in ("start", "end"):
                if c in cur.visits and not cur.doubled:
                    cur.children.append(Node(c, cur.path, cur.visits, cur.doubled))
        queue.extend(cur.children[:])
    return root

def traverse_tree(root):
    if root.children == []:
        if root.name == "end":
            return 1
        else:
            return 0
    else:
        path_count = 0
        for c in root.children:
            path_count += traverse_tree(c)
        return path_count


with open("input") as f:
    inp = f.readlines()

visited = set()
graph = {}
for line in inp:
    from_cave, to_cave = line.strip().split('-')
    if from_cave in graph:
        graph[from_cave].append(to_cave)
    else:
        graph[from_cave] = [to_cave]
    if from_cave != "start" and to_cave != "end":
        if to_cave in graph:
            graph[to_cave].append(from_cave)
        else:
            graph[to_cave] = [from_cave]
graph["end"] = []

# print(graph)
tree = build_tree(graph)
paths = traverse_tree(tree)

print("total =", paths)
