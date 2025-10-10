import pydot

# Load the DOT file
(graph,) = pydot.graph_from_dot_file("schema_diagram.dot")

# Save as PNG
graph.write_png("schema_diagram.png")