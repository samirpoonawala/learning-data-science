from s5v1 import *

def plot_all_bars(prices_in_float, exported_figure_filename):
    prices = list(map(int, prices_in_float))
    X = numpy.arange(len(prices))
    width = 0.25
    plt.bar(X+width, prices, width) 
    plt.xlim([0,5055])
    plt.savefig(exported_figure_filename)

def create_bar_chart(price_groups, exported_figure_filename):
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    plt.style.use('ggplot')
    colors=plt.rcParams['axes.color_cycle']
     
    for group in price_groups:
        ax.bar(group, price_groups[group], color=colors[group%len(price_groups)])

    labels = ["$0-50", "$50-100", "$100-150", "$150-200", "$200-250", "$250+"]
    ax.legend(labels)

    ax.set_title('Amount of Ties at price points')
    ax.set_xlabel('Tie Price ($)')
    ax.set_xticklabels(labels, ha='left')
    ax.set_xticks( range(1, len(price_groups)+1) )
    ax.set_ylabel('Number of Ties')

    plt.grid(True)
    fig.savefig(exported_figure_filename)

from collections import Counter
def group_prices_by_range(prices_in_float):
    
    tally = Counter()

    for item in prices_in_float:
        bucket = 0
        rounded_price = round(item, -1)
        if rounded_price >= 0 and rounded_price <= 50:
            bucket = 1
        elif rounded_price >= 50 and rounded_price <= 100:
            bucket = 2
        elif rounded_price >= 100 and rounded_price <= 150:
            bucket = 3
        elif rounded_price >= 150 and rounded_price <= 200:
            bucket = 4
        elif rounded_price >= 200 and rounded_price <= 250:
            bucket = 5
        elif rounded_price >= 250:
            bucket = 6
        else:
            bucket = 7

        tally[bucket] += 1
    return tally

price_groups = group_prices_by_range(price_in_float)
create_bar_chart(price_groups, "_charts/s5-price_in_groups.png") 
