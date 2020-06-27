import plotly.express as px
from django.shortcuts import render


def plot_graphic(request):
    df = px.data.election()
    fig = px.scatter_3d(df, x="Joly", y="Coderre", z="Bergeron", color="winner", size="total", hover_name="district",
                        symbol="result", color_discrete_map={"Joly": "blue", "Bergeron": "green", "Coderre": "red"})

    graph = fig.to_html(full_html=False, default_height=900, default_width=900)
    context = {'graph': graph}
    return render(request, 'plotly_graphics/plot.html', context=context)
