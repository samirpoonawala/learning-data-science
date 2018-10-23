from s5v3 import *

def create_line_chart2(data_sample, title, exported_figure_filename):
  fig = plt.figure()
  ax = fig.add_subplot(1,1,1)
  
  prices = (sorted(map(float, data_sample)))
  
  x_axis_ticks = list(range(len(data_sample)))
  ax.plot(x_axis_ticks, prices, linewidth=2)
  ax.set_title(title)
  ax.set_xlim([0, len(data_sample)])
  ax.set_xlabel("[THIS IS THE X]")
  ax.set_ylabel("[THIS IS THE Y]")
  
  fig.savefig(exported_figure_filename)

#create_line_chart2([float(x[2]) for x in jcrew_ties[1:]], "THIS IS THE TITLE", "labels.png")


