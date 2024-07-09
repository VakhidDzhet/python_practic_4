import pandas as pd
import seaborn as sns
from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import certifi
import os

os.environ['SSL_CERT_FILE'] = certifi.where()

df = sns.load_dataset('penguins')

app = Dash(__name__)

app.layout = html.Div([
    html.H1("Penguins Body Mass Distribution"),
    dcc.Graph(id='boxplot-graph'),
    html.Label("Minimum Body Mass (g)"),
    dcc.Slider(
        id='mass-slider',
        min=df['body_mass_g'].min(),
        max=df['body_mass_g'].max(),
        value=df['body_mass_g'].min(),
        marks={int(mass): str(int(mass)) for mass in df['body_mass_g'].quantile([0, 0.25, 0.5, 0.75, 1]).values},
        step=100
    ),
    html.Label("Select Sex"),
    dcc.Dropdown(
        id='sex-dropdown',
        options=[{'label': sex, 'value': sex} for sex in df['sex'].dropna().unique()],
        value=df['sex'].dropna().unique().tolist(),
        multi=True
    )
])

@app.callback(
    Output('boxplot-graph', 'figure'),
    [Input('mass-slider', 'value'),
     Input('sex-dropdown', 'value')]
)
def update_boxplot(min_mass, selected_sex):
    filtered_df = df[(df['body_mass_g'] >= min_mass) & (df['sex'].isin(selected_sex))]
    fig = px.box(filtered_df, x='species', y='body_mass_g', color='species', title="Body Mass Distribution by Species")
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
