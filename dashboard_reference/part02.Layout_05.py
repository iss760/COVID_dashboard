# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html


# 시트 스타일 선택
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# 앱 설정
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# 레이아웃 설정
app.layout = html.Div([
    # Dropdown 설정
    html.Label('Dropdown'),
    dcc.Dropdown(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': u'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value='MTL'
    ),

    # Multi-Select Dropdown 설정
    html.Label('Multi-Select Dropdown'),
    dcc.Dropdown(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': u'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value=['MTL', 'SF'],
        multi=True
    ),

    # Checkboxes 설정
    html.Label('Checkboxes'),
    dcc.Checklist(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': u'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value=['MTL', 'SF']
    ),

    # Text Input 설정
    html.Label('Text Input'),
    dcc.Input(value='MTL', type='text'),

    # Slider 설정
    html.Label('Slider'),
    dcc.Slider(
        min=0,
        max=9,
        marks={i: 'Label {}'.format(i) if i == 1 else str(i) for i in range(1, 9)},
        value=1
    ),
], style={'columnsCount': 1})


if __name__ == '__main__':
    # 앱 설정
    app.run_server(debug=True)