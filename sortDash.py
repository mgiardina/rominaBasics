import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash
from dash.dependencies import Input, Output, State
import plotly.graph_objects as go
from randomarray import GenerateRandomArray
from nanoseconds import CurrentNanoSeconds
from sorting import *

AWS_LOGO = "https://upload.wikimedia.org/wikipedia/commons/thumb/9/93/Amazon_Web_Services_Logo.svg/1024px-Amazon_Web_Services_Logo.svg.png"

numbers_list = [{'label': '5000', 'value': 5000},
                {'label': '10000', 'value': 10000},
                {'label': '15000', 'value': 15000},
                {'label': '20000', 'value': 20000},
                {'label': '25000', 'value': 25000},
                {'label': '40000', 'value': 40000},
                {'label': '50000', 'value': 50000}]

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.title = 'AWS Dash Sorting Demo'

randomArrayCollapse = html.Div(
    [
        dbc.Button(
            "Display Random Array",
            id="randomArrayCollapse-button",
            className="mb-3",
            color="primary",
            n_clicks=0,
        ),
        dbc.Collapse(
            dbc.Card(dbc.CardBody(html.Div(id='randomArrayText'))),
            id="randomArrayCollapse",
            is_open=False,
        ),
    ]
)

sortedArrayCollapse = html.Div(
    [
        dbc.Button(
            "Display Sorted Array",
            id="sortedArrayCollapse-button",
            className="mb-3",
            color="primary",
            n_clicks=0,
        ),
        dbc.Collapse(
            dbc.Card(dbc.CardBody(html.Div(id='sortedArrayText'))),
            id="sortedArrayCollapse",
            is_open=False,
        ),
    ]
)

navbar = dbc.Navbar(html.Div([
    html.A(
                    dbc.Row([
                        html.Img(src=AWS_LOGO, height="30px",
                                 className="mt-2 mr-2"),
                        dbc.NavbarBrand("Dash Sorting Demo by Romina Mezher", style={
                                        "text-decoration": "none"}),
                    ],
                        align="right",
                        no_gutters=True,
                        className="mb-12",
                        style={'padding': '10px'}
                    )
                    ),
]))

app.layout = html.Div([navbar,
                       dcc.Store(id='arrayStore'),
                       html.Div(className="ml-4",
                                children=[html.H2(children="Romina Basic Training. Sorting Demo", className='mb-1', style={'margin-top': '30px'}),
                                          html.Br(),
                                          html.P(
                                    'This is a sorting algorithm performance comparison for a random array with less than 50000 elements.'),
                                    html.P(
                                    'We are comparing Bubble, Selection & Insertion. Merge & QuickSort are out of current scope. More Info at the bottom.'),
                                    html.Br(),
                                    html.Div(
                                    children=[
                                        html.H5('Select array size'),
                                        dcc.Dropdown(id="ddlNumber",
                                                     options=numbers_list, value=1,
                                                     style={
                                                         'font-size': '15px', 'white-space': 'nowrap', 'text-overflow': 'ellipsis'}
                                                     ),
                                        html.Br(),
                                    ], style={'width': '25%', 'margin-top': '5px'}),
                                    html.Div(
                                    children=[
                                        html.Div(
                                            children=[
                                                dbc.Row(
                                                    children=[
                                                        dbc.Col(
                                                            randomArrayCollapse, md=12)
                                                    ]
                                                ),
                                                dbc.Row(
                                                    children=[
                                                        dbc.Col(
                                                            sortedArrayCollapse, md=12)
                                                    ]
                                                )
                                            ]
                                        ),
                                        html.Br(),
                                        html.H5('Results'),
                                        html.Div(id='performanceText'),
                                        dcc.Graph(id='performanceGraph'),
                                        html.Br(),
                                        html.H5('Performance'),
                                        html.P('Insertion algorithm has better performace for the case of smaller arrays because it uses an average far fewer operations per single exchange. It splits the array and works on the unsorted part of it. Merge and Quick sorting are based on divide and conquer approach with slight differences. They both have good performances due of the use of array partition and are more effective with a couple of million items array. Bubble algorithm is the worst it terms of performace because all the comparisons are made even if the array is already sorted. This increases the use of computer memory (RAM) as the array elements increase.'),
                                        html.Br(),
                                        html.Img(src='https://www.pngfind.com/pngs/m/660-6607266_png-file-svg-document-icon-png-transparent-png.png', width='50px', className='mr-2'),
                                        dcc.Link(
                                            'Documentation', href='https://github.com/mgiardina/rominaBasics/blob/main/sorting.md', target='_blank'),
                                        html.Br(),
                                        html.Img(src='https://dash.plotly.com/assets/images/language_icons/python_50px.svg', className='mr-2'),
                                        dcc.Link(
                                            'Code (GITHUB)', href='https://github.com/mgiardina/rominaBasics', target='_blank'),
                                        html.Br(),
                                        html.Br(),
                                        html.Br()
                                    ],
                                ),
                                ]
                                )]
                      )


@app.callback(
    [Output('randomArrayText', 'children'),
     Output('arrayStore', 'data')],
    [Input('ddlNumber', 'value')])
def update_output(value):
    randomArray = GenerateRandomArray(value)
    return formatArray(randomArray), randomArray


@app.callback(
    Output("randomArrayCollapse", "is_open"),
    [Input("randomArrayCollapse-button", "n_clicks")],
    [State("randomArrayCollapse", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


@app.callback(
    Output("sortedArrayCollapse", "is_open"),
    [Input("sortedArrayCollapse-button", "n_clicks")],
    [State("sortedArrayCollapse", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


@app.callback(
    [Output('performanceGraph', 'figure'),
     Output('performanceText', 'children'),
     Output('sortedArrayText', 'children')],
    Input('arrayStore', 'data')
)
def sortingProc(data):

    start = CurrentNanoSeconds()
    SelectionSort(data)
    end = CurrentNanoSeconds()
    executionTimeSelection = end-start

    start = CurrentNanoSeconds()
    arrayBubbleSort = BubbleSort(data)
    end = CurrentNanoSeconds()
    executionTimeBubble = end-start

    start = CurrentNanoSeconds()
    InsertionSort(data)
    end = CurrentNanoSeconds()
    executionTimeInsertion = end-start

    if (executionTimeBubble != 0):

        returnedHtml = [
            html.Br(),
            html.H5(
                f'Insertion sorting algorithm execution took {executionTimeInsertion} nanoseconds'),
            html.H5(
                f'Selection sorting algorithm execution took {executionTimeSelection} nanoseconds'),
            html.H5(
                f'Bubble sorting algorithm execution took {executionTimeBubble} nanoseconds')
        ]
    else:

        returnedHtml = ''

    sortAlgorithms = ['Insertion', 'Selection', 'Bubble']

    results = [executionTimeInsertion,
               executionTimeSelection, executionTimeBubble]

    fig = go.Figure(data=[go.Bar(
        x=sortAlgorithms, y=results, text=results, textposition='auto', textfont_size=19)])

    fig.update_traces(marker_color='#86B049',
                      marker_line_width=1.5, opacity=0.9)

    fig.update_layout(xaxis_tickfont_size=18,
                      yaxis=dict(
                          title='Nanoseconds',
                          titlefont_size=18,
                          tickfont_size=18
                      ),
                      width=1000, height=600,
                      plot_bgcolor='#cdcdcd'
                      )

    return(fig, returnedHtml, formatArray(arrayBubbleSort))


def formatArray(array):
    return ", ".join(str(item) for item in array)


if __name__ == "__main__":
    app.run_server(debug=True)
