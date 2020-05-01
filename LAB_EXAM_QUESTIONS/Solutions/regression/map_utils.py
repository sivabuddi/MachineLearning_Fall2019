import matplotlib.pyplot as plot
import seaborn as sns


def scatter_plot(x_axis_data, y_axis_data, x_label, y_label, figure_label):
    plot.scatter(x_axis_data, y_axis_data, alpha=.75, color='b')
    plot.xlabel(x_label)
    plot.ylabel(y_label)
    plot.title(figure_label)
    plot.show()


def heat_map(matrix):
    sns.heatmap(matrix, xticklabels=matrix.columns, yticklabels=matrix.columns, annot=True)
