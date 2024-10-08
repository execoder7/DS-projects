import dash 
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

app = dash.Dash(__name__)

df = pd.read_csv('data/intro_bees.csv')

df = df.groupby(["State",'ANSI','Affected by','Year','state_code']).agg({'Pct of Colonies Impacted':'mean'}).reset_index()

# App layout

app.layout = html.Div([
    
    html.H1("Web App Dashboard", style={"text-align":'center'}),
    
    dcc.Dropdown(
        id="slct_year",
        options=[{'label':year, 'value': int(year)} for year in df['Year'].unique()],
        multi=False,
        value= df['Year'].unique()[0],
        style={'width':'40%'}
    ),
    
    html.Div(id='output_container', children=[]),
    html.Br(),
    
    dcc.Graph(id='my_bees_map', figure={})
    
])

# Callback 


@app.callback(
    [Output('output_container','children' ),
     Output(component_id='my_bees_map', component_property='figure' )
     ],
    [Input('slct_year','value') ]
)

def update_graph(option_slct):
    
    container = f"Year: {option_slct}"
    
    dff = df.copy()
    dff = dff.loc[(dff['Year'] == option_slct) & (dff['Affected by'] == 'Varroa_mites') ]
    
    # Plotly express
    
    fig = px.choropleth(
        dff,
        locationmode="USA-states",
        locations='state_code',
        scope="usa",
        color="Pct of Colonies Impacted",
        color_continuous_scale=px.colors.sequential.YlOrRd,
        labels={'Pct of Colonies Impacted': "% of the bees"},
        template="plotly_dark"
    )

    return container, fig


# Run app
if __name__ == '__main__':
    app.run_server(debug=True)


