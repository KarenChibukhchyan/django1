# import plotly.express as px
from django.shortcuts import render


def plot_graphic(request):
    # df = px.data.iris()
    # fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species",
    #                  size='petal_length', hover_data=['petal_width'])
    # graph = fig.to_html(full_html=False, default_height=500, default_width=700)
    # context = {'graph': graph}
    return render(request, 'plotly_graphics/plot.html', context='context')
