import json
import plotly.graph_objects as go

import pprint
from pathlib import Path
from collections import Counter

count = Counter()
beer_json_file_path = Path.home() / "Chris-Untappd-History.json"
with open(beer_json_file_path,"r") as beerfile:
    beer_json = json.load(beerfile)


for beer in beer_json:
    count[beer['brewery_name']] += 1
    pprint.pprint(beer)
x = []
y = []

most_common = count.most_common(30)
for tuple in most_common:
    x.append(tuple[0])
    y.append(tuple[1])

fig = go.Figure([go.Bar(x=x,y=y)])


fig.update_layout(
    title=go.layout.Title(
        text="My 30 All Time Top Breweries",
        xref="paper",
        x=0
    ),
    xaxis=go.layout.XAxis(
        title=go.layout.xaxis.Title(
            text="Number of Beers Checked In",
        )
    ),
    yaxis=go.layout.YAxis(
        title=go.layout.yaxis.Title(
            text="Breweries",
        )
    )
)

fig.show()
# pprint.pprint(count)
