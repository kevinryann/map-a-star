import matplotlib.pyplot as plt
import plotly.graph_objects as go
import point

def visualize(listPoints) : # This function visualizes the graph in cartesian plane
    with open("../test/input1.txt", "r") as f :
        # Initializing empty list x and y for edge
        edge_x = []
        edge_y = []

        # Appending edges with according to format
        for elmt in listPoints :
            for elmt2 in elmt.route :
                edge_x.append(elmt.x)
                edge_x.append(elmt2.x)
                edge_x.append(None)
                edge_y.append(elmt.y)
                edge_y.append(elmt2.y)
                edge_y.append(None)

    # Plotting with scatter
    edge_trace = go.Scatter(
        x=edge_x, y=edge_y,
        line=dict(width=1, color='black'),
        hoverinfo='none',
        mode='lines')

    # Initializing empty list x and y for node
    node_x = []
    node_y = []

    # Appending x and y to list node
    for elmt in listPoints :
        node_x.append(float(elmt.x))
        node_y.append(float(elmt.y))

    # Make traces
    node_trace = go.Scatter(
        x = node_x, y=node_y,
        mode = 'markers',
        marker = dict(
            line_width=5))
        
    # Make figure
    fig = go.Figure(data=[edge_trace, node_trace],
             layout = go.Layout( # Set layout
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
            'center' : {'lat':0, 'lon':50},
            'style' : "stamen-terrain",
            'zoom' : 1,
            'center' : {'lat':0, 'lon':50}
        }
    )

    fig.show()