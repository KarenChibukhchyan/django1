import plotly.express as px
from django.shortcuts import render


def plot_graphic(request):
    fig = px.scatter({'my_x': [0, 1, 2, 3, 4], 'my_y': [0, 1, 4, 9, 16]}, x='my_x', y='my_y', hover_name=['a', 'b', 'c', 'd', 'e'])

    graph = fig.to_html(full_html=False, default_height=500, default_width=700)
    context = {'graph': graph}
    return render(request, 'plotly_graphics/plot.html', context=context)
