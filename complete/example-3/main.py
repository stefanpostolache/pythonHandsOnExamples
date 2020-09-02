import matplotlib.pyplot as plt

"""
This module contains functions to create a graph of the averages of other graphs
A graph is pair of lists of numbers, one list for the abscissas and another for the ordinates, 
both lists having the same size.
"""

def averages(graphs):
    """
    Function that takes a list of graphs and creates another graph of which the ordinates are the
    averages of the ordinates of other graphs.

    Args:
        graphs (list): list of graphs, all having the same abscissas.
    
    Return:
        tuple: graph of which the ordinates are the averages of the ordinates of the graphs in the list of graphs

    one graph with one ordinate and one abscissa only
    >>> averages([([1], [5])])
    ([1], [5.0])

    multiple graphs with multiple abscissas
    >>> abcissas = list(range(1, 4))
    >>> graficos = [(abcissas, [1, 2, 3]), (abcissas, [4, 5, 6]), (abcissas, [7, 8, 9])]
    >>> averages(graficos)
    ([1, 2, 3], [4.0, 5.0, 6.0])

    multiple graphs of which some are invalid one having more ordinates than abscissas
    >>> graficos = [(abcissas, [1, 2, 3]), (abcissas, [4, 5, 6]), (abcissas, [7, 8, 9, 10])]
    >>> averages(graficos)
    graphs must be a list of graphs, and all graphs must have the same abscissas

    multiple graphs of which one is invalid because it has different abscissas than the others
    >>> graficos = [(abcissas, [1, 2, 3]), (abcissas, [4, 5, 6]), ([2,3,4], [7, 8, 9])]
    >>> averages(graficos)
    graphs must be a list of graphs, and all graphs must have the same abscissas
    """

    try:
        assert list(filter(lambda graph: len(graph[0]) == len(graph[1]) and graph[0] == graphs[0][0], graphs)) == graphs, "graphs must be a list of graphs, and all graphs must have the same abscissas"

        abscissas = graphs[0][0]
        ordinates = []

        for position in range(len(abscissas)):
            # ordinate_sum = 0
            # for graph in graphs:
            #     ordinate_sum += graph[1][position]
            # ordinates.append(ordinate_sum/len(graphs))
            ordinates.append(sum([graph[1][position] for graph in graphs])/len(graphs))

        return (abscissas, ordinates)
    except AssertionError as ae:
        print(ae)

def showAveragesInGraph(averages):
    """
    Plots averages in a bar plot

    Args:
        averages (tuple): graf containing averages of other graphs
    """
    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1])
    ax.bar(*averages)
    plt.show()


if __name__=='__main__':
    import doctest
    doctest.testmod()