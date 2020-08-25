from graphviz import Digraph
from graphviz import Source
import os
stream = os.popen('adr generate graph')
graph_source = stream.read()
source_file = './doc/architecture/ADR_Dependencies'
with open(source_file,'w') as graph_write:
    graph_write.writelines(graph_source)

#dot = Digraph(comment='ADR Graph')
#dot.source()

s = Source.from_file(source_file)
s.render(view=False,format='png')


