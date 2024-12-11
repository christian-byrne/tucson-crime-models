from graphviz import Digraph

# Create a new directed graph
diagram = Digraph(comment='Conceptual Framework')

# Set global attributes for aesthetics
diagram.attr(rankdir='TB', size='8,5')  # Top-to-bottom layout, reasonable size
diagram.attr('node', shape='box', style='rounded, filled', color='lightblue', fontname='Arial')
diagram.attr(dpi='300')  # Set high resolution

# Add nodes
diagram.node('A', 'Infrastructure Features')
diagram.node('B', 'Crime Density')
diagram.node('C', 'Mean Education Levels')

# Add edges with labels
diagram.edge('A', 'B', label='Linear Regression')
diagram.edge('B', 'C', label='SVM Classifier')

# Save and render the diagram
diagram.render('conceptual_framework', format='png', cleanup=True)
diagram.view()
