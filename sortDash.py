import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash
from dash.dependencies import Input, Output,State
import plotly.graph_objects as go
from randomarray import GenerateRandomArray
from nanoseconds import CurrentNanoSeconds
from sorting import *

AWS_LOGO = "https://upload.wikimedia.org/wikipedia/commons/thumb/9/93/Amazon_Web_Services_Logo.svg/1024px-Amazon_Web_Services_Logo.svg.png"

numbers_list= [{'label': '1', 'value': 1},
             {'label': '10', 'value': 10},
             {'label': '100', 'value': 100},
             {'label': '1000', 'value': 1000},
             {'label': '10000', 'value': 10000}]
         

app = dash.Dash(__name__,external_stylesheets=[dbc.themes.COSMO])

app.title = 'AWS Dash Sorting Demo'

navbar = dbc.Navbar(dbc.Container([
                html.A(
                dbc.Row([
                        html.Img(src=AWS_LOGO, height="30px",className="mt-2 mr-2"),
                        dbc.NavbarBrand("Dash Sorting Demo by Romina Mezher", style={"text-decoration" : "none"}),
                    ],
                    align="right",
                    no_gutters=True,
                    className="mb-1",
                )
                ),
        ]))

app.layout = html.Div([navbar,
                html.Div(className = 'ml-4',
                children=[html.H1(children="Sorting Demo",className = 'mb-3'),
                        html.Br(),
                        html.H3(children="This is a sorting algorithm performance comparison for a" 
                            " random array with less of 10000 elements"),
                        html.Br(),
                    html.Div(
                        children=[    
                            html.H5('Select array size'),
                            dcc.Dropdown(id="ddlNumber",
                                options=numbers_list,value=1,
                                style = {'font-size': '15px', 'white-space': 'nowrap', 'text-overflow': 'ellipsis'}
                                ),
                            dbc.Button("Submit", id="btnInput", outline=True,color="success", 
                                className="mt-3 mb-5"),
                        ],style = {'width' : '25%', 'margin-top' : '5px'}),
                    html.Div(
                        children=[
                            dcc.Graph(id='performanceGraph'),
                            html.Div(id='performanceText')
                        ],
                    ),
            ]        
                )]
            )


@app.callback(
    [Output('performanceGraph', 'figure'),
    Output('performanceText', 'children')],
    Input('btnInput', 'n_clicks'),
    State('ddlNumber', 'value'),
)

def sortingProc(n_clicks,value):

    array = GenerateRandomArray(value)
    
    randomArray = array
    print(randomArray)
    
    start = CurrentNanoSeconds()
    arraySelectSort = SelectionSort(array)
    end = CurrentNanoSeconds()
    executionTimeSelec = end-start

    start = CurrentNanoSeconds()
    arrayBubbleSort = BubbleSort(array)
    end = CurrentNanoSeconds()
    executionTimeBubb = end-start

    start = CurrentNanoSeconds()
    arrayInsertionSort = InsertionSort(array)
    end = CurrentNanoSeconds()
    executionTimeInser = end-start

    returnedHtml = [html.H5(f'Random array: {randomArray}'),
                    html.Br(),
                    html.H5(f'Insertion sorting algorithm execution took {executionTimeInser} nanoseconds'),
                    html.H5(f'Selection sorting algorithm execution took {executionTimeSelec} nanoseconds'),
                    html.H5(f'Bubble sorting algorithm execution took {executionTimeBubb} nanoseconds'),
                    html.Br(),
                    html.H5(f'Sorted random array: {arrayBubbleSort}')]
    
    sortAlgorithms=['Insertion','Selection', 'Bubble']

    results= [executionTimeInser,executionTimeSelec,executionTimeBubb]

    fig = go.Figure(data = [go.Bar(
        x=sortAlgorithms, y=results, text = results,textposition = 'auto',textfont_size=19)])

    fig.update_traces(marker_color='#86B049',
                  marker_line_width=1.5, opacity=0.9)    

    fig.update_layout(title='Sorting algorithms performance',
                xaxis_tickfont_size=18,
                yaxis=dict(
                title='Nanoseconds',
                titlefont_size=18,
                tickfont_size=18
                ),
                width=1000, height=600,
                plot_bgcolor = '#cdcdcd'
    )            

    return(fig,returnedHtml)
        
   


if __name__ == "__main__":
    app.run_server(debug=True)