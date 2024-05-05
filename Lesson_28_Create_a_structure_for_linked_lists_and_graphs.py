class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Edge:
    def __init__(self, source, destination, distance=None, cost=None, directed=False):
        self.source = source
        self.destination = destination
        self.distance = distance
        self.cost = cost
        self.directed = directed


class InventoryList:
    def __init__(self):
        self.head = None

    def add_item(self, item):
        new_node = Node(item)
        if not self.head:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node


class LogisticLocation:
    def __init__(self, name, capacity=0, inventory=0):
        self.name = name
        self.capacity = capacity
        self.inventory = inventory
        self.inventory_list = InventoryList()
        self.edges = []

    def add_inventory(self, item):
        self.inventory_list.add_item(item)
        self.inventory += 1

    def add_edge(self, edge):
        self.edges.append(edge)


class LogisticGraph:
    def __init__(self, directed=False):
        self.nodes = []
        self.edges = []
        self.directed = directed

    def add_node(self, node):
        self.nodes.append(node)

    def add_edge(self, source, destination, distance=None, cost=None):
        edge = Edge(source, destination, distance, cost, self.directed)
        self.edges.append(edge)
        source.add_edge(edge)
        if not self.directed:
            destination.add_edge(edge)


# Logistic graph
logistic_graph = LogisticGraph(directed=True)

# Logistic locations
warehouse_a = LogisticLocation("Warehouse Washington")
warehouse_b = LogisticLocation("Warehouse Florida")
factory = LogisticLocation("Factory")
retail_store = LogisticLocation("Retail Store Alabama")

# Add nodes to logistic graph
logistic_graph.add_node(warehouse_a)
logistic_graph.add_node(warehouse_b)
logistic_graph.add_node(factory)
logistic_graph.add_node(retail_store)

# Edges
logistic_graph.add_edge(warehouse_a, factory, distance=50, cost=200)
logistic_graph.add_edge(warehouse_b, factory, distance=70, cost=250)
logistic_graph.add_edge(factory, retail_store, distance=30, cost=150)
logistic_graph.add_edge(factory, warehouse_a, distance=50, cost=200)
logistic_graph.add_edge(factory, warehouse_b, distance=70, cost=250)

# Inventory to a location
warehouse_a.add_inventory("Steel Rodes")
warehouse_a.add_inventory("Steel Plates")

# Inventory
current = warehouse_a.inventory_list.head
print("Inventory at Warehouse Washington:")
while current:
    print(current.value)
    current = current.next
