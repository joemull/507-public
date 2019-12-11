# https://blog.heptanalytics.com/2018/08/07/flask-plotly-dashboard/

import plotly
import plotly.graph_objs as go
import json

class MuseumSite():
    def __init__(self,locatedWork):
        self.name = locatedWork.currentRepo
        self.lat = locatedWork.lat
        self.lng = locatedWork.lng
        self.marker = 'circle'
        self.color = 'blue'

    def make_label(self,sortedWorks):
        self.workList = ""+ self.name +"<br>"
        for work in sortedWorks:
            if self.name == work.currentRepo:
                # self.workList += "<a href=/object/"+ work.pid +">"
                self.workList += "" + work.titleText + "<br>"
                # self.workList += work.imageReferences['primaryImageSmall'] + "<br>"
                # self.workList += "</a>"
            # print(self.label)

def map_for(locatedWorks):

    sites = []
    sortedWorks = sorted(locatedWorks, key = lambda work:work.currentRepo)
    for work in sortedWorks:
        if work.currentRepo not in [site.name for site in sites]:
            site = MuseumSite(work)
            site.label = site.make_label(sortedWorks)
            sites.append(site)

    labels = [site.name for site in sites]
    lat_vals = [site.lat for site in sites]
    lon_vals = [site.lng for site in sites]
    markers = [site.marker for site in sites]
    colors = [site.color for site in sites]
    hovertext = [site.workList for site in sites]

    min_lat = float(min(lat_vals))
    max_lat = float(max(lat_vals))
    min_lon = float(min(lon_vals))
    max_lon = float(max(lon_vals))
    height = max_lat - min_lat
    width = max_lon - min_lon
    pad = .2 * (height + width) / 2

    lat_axis = [min_lat-pad,max_lat+pad]
    lon_axis = [min_lon-pad,max_lon+pad]

    center_lat = (min_lat + max_lat) / 2
    center_lon = (min_lon + max_lon) / 2

    fig = go.Figure(data=go.Scattergeo(
        lat = lat_vals,
        lon = lon_vals,
        text = labels,
        hovertext = hovertext,
        mode = 'markers',
        marker = dict (
            size = 14,
            symbol = markers,
            color = colors,
        )
    ))

    layout = dict(
        title = 'Results',
        geo = dict(
            scope='world',
            projection=dict( type='albers usa' ),
            showland = True,
            landcolor = "rgb(250, 250, 250)",
            subunitcolor = "rgb(100, 217, 217)",
            countrycolor = "rgb(217, 100, 217)",
            lataxis = {'range': lat_axis},
            lonaxis = {'range': lon_axis},
            center= {'lat': center_lat, 'lon': center_lon },
            countrywidth = 3,
            subunitwidth = 3
        )
    )

    # fig.update_layout(layout)

    mapJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    layoutJSON = json.dumps(layout, cls=plotly.utils.PlotlyJSONEncoder)

    return mapJSON, layoutJSON
