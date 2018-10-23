# CREATE PDF

import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from s6v1 import *

def plot_minimal_graph(tally, columns, *args):
  plt.style.use('bmh')
  fig = plt.figure(dpi=200)
  colors = plt.rcParams['axes.color_cycle']
  
  # white background to use less color ink
  ax = plt.subplot(111, axisbg='white')
  
  # plot bars and screate text labels for the table
  for priceBucket in tally:
    ax.bar(priceBucket, tally[priceBucket], color=colors[priceBucket%len(tally)])
    ax.annotate(r"%d" % (tally[priceBucket]),
               (priceBucket+0.2, tally[priceBucket]),
               va="bottom", ha="center")
    
    # include a legend
    ax.legend(columns)
    
    # remove distracting lines on top, left, and right
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    
    # remove distracting tick marks
    ax.yaxis.set_ticks_position('none')
    ax.xaxis.set_ticks_position('none')
    
    # add chart title and axes labels
    plt.xlabel("Tie Price", fontsize = 13)
    plt.ylabel("Number of Ties", fontsize = 13)
    plt.title("Chart # 1")
    
    # add labels to bars along x axes
    x = range(1, len(tally)+1)
    plt.xticks(x, columns, rotation='horizontal',ha='left')
    
    return fig
  
def plot_graph_with_table(cell_text, row_text, columns):
  plt.style.use('ggplot')
  fig = plt.figure()
  
  
  # Include table
  ax2 = fig.add_subplot(111)
  ax2.axis("off")
  
  the_table = ax2.table(cellText=cell_text, rowLabels=row_text, colLabels=columns, loc='center right')
  
pp = PdfPages('my_report.pdf')

plot1 = plot_minimal_graph(price_groups, columns)
pp.savefig(plot1, bbox_inches='tight')

table_text = build_table_text(brand_and_price_data, brands)
plot2 = plot_graph_with_table(table_text[0], table_text[1], columns)
plt.save(plot2, bbox_inches='tight')

pp.close()