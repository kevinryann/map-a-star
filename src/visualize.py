import matplotlib.pyplot as plt
import plotly.graph_objects as go
import point

def visualize(listPoints) : # This function visualizes the graph in cartesian plane
    with open("../test/input1.txt", "r") as f :
        edge_x = []
        edge_y = []

        for elmt in listPoints :
            for elmt2 in elmt.route :
                edge_x.append(elmt.x)
                edge_x.append(elmt2.x)
                edge_x.append(None)
                edge_y.append(elmt.y)
                edge_y.append(elmt2.y)
                edge_y.append(None)

    edge_trace = go.Scatter(
        x=edge_x, y=edge_y,
        line=dict(width=1, color='black'),
        hoverinfo='none',
        mode='lines')

    node_x = []
    node_y = []

    for elmt in listPoints :
        node_x.append(float(elmt.x))
        node_y.append(float(elmt.y))

    node_trace = go.Scatter(
        x = node_x, y=node_y,
        mode = 'markers',
        marker = dict(
            line_width=5))
        
    fig = go.Figure(data=[edge_trace, node_trace],
             layout = go.Layout(
                title = 'Visualisasi Points',
                titlefont_size = 16,
                showlegend = False,
                margin = dict(b = 20, l = 5, r = 5, t = 40),
                xaxis = dict(showgrid = True, zeroline = True, showticklabels = True),
                yaxis = dict(showgrid = True, zeroline = True, showticklabels = True)
                ))
    fig.show()


def visualizee(listPoints, path, start, end) : # This functions visualizes the routes in world map
    fig = go.Figure()

    for i in range(len(path)-1):
        fig.add_trace(go.Scattermapbox(
            mode = "markers+lines",
            lon = [path[i].y, path[i+1].y],
            lat = [path[i].x, path[i+1].x],
            marker = {"size" : 10, "color" : "black"},
            line_color = "blue",
        ))

    fig.add_trace(go.Scattermapbox(
                mode = "markers+text",
                lon = [start.y],
                lat = [start.x],
                marker = {"size" : 10, "color" : "red"}, 
                text = ["Start"],
                textposition = "top center",
                name = "Start"
            ))
    
    fig.add_trace(go.Scattermapbox(
                mode = "markers+text",
                lon = [end.y],
                lat = [end.x],
                marker = {"size" : 10, "color" : "red"}, 
                text = ["End"],
                textposition = "top center",
                name = "End"
            ))

    fig.update_layout(
        margin = {'l':0, 't':0, 'b':0, 'r':0},
        mapbox = {
            'center' : {'lon':50, 'lat':0},
            'style' : "stamen-terrain",
            'zoom' : 1,
            'center' : {'lon':50, 'lat':0}
        }
    )

    fig.show()