import networkx as nx
import matplotlib.pyplot as plt

# ข้อมูลเส้นทาง
paths = [
    {'source': 'A', 'target': 'B', 'distance': 40},
    {'source': 'A', 'target': 'C', 'distance': 40},
    {'source': 'B', 'target': 'D', 'distance': 50},
    {'source': 'B', 'target': 'C', 'distance': 20},
    {'source': 'B', 'target': 'F', 'distance': 30},
    {'source': 'D', 'target': 'E', 'distance': 30},
    {'source': 'F', 'target': 'D', 'distance': 30},
    {'source': 'C', 'target': 'E', 'distance': 50},
]

# สร้างกราฟ
G = nx.Graph()

# เพิ่มเส้นทางลงในกราฟ
for path in paths:
    G.add_edge(path['source'], path['target'], weight=path['distance'])

# สร้างเเผนภาพของกราฟ
pos = nx.spring_layout(G)  # กำหนดตำแหน่งของโหนด

# กำหนดสีของโหนด 'E' เป็นสีเหลือง
node_colors = ['yellow' if node == 'E' else 'green' if node == 'A' else 'gray' for node in G.nodes()]

# ปรับความหนาและสีของเส้นทาง
nx.draw(G, pos, with_labels=True, width=2, edge_color='red', node_color=node_colors, node_size=500)

# ดึงข้อมูลระยะทาง
labels = nx.get_edge_attributes(G, 'weight')

# ปรับตำแหน่งของตัวเลขเส้นทาง
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_color='blue')

plt.show()