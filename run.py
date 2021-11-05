# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import pandas as pd

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px


DATA_PATH = './COVID_infection_prc.csv'
OPTION = {'확진자': 'decideCnt',
          '사망자': 'deathCnt',
          '치료중 환자': 'careCnt',
          '치료완료': 'clearCnt',
          '검사자': 'examCnt'}


# 시트 스타일 선택
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
# 앱 설정
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# load datasets
df = pd.read_csv(DATA_PATH, index_col=0)

# 레이아웃 설정
app.layout = html.Div(children=[
    # 제목 배치
    html.H1(children='Dash'),

    # Dropdown 설정
    html.Label('Check'),
    dcc.Dropdown(
        id='select-data',
        options=[{'label': k, 'value': v} for k, v in OPTION.items()],
        value=list(OPTION.values())[0]
    ),

    # 그래프 배치
    dcc.Graph(
        id='main-graph',
        figure=px.bar(df, x='date', y='decideCnt', barmode='group')      # Default 그래프 설정
    ),

    html.Label('Slider'),
    dcc.Slider(
        min=0,
        max=9,
        marks={i: 'Label {}'.format(i) if i == 1 else str(i) for i in range(1, 9)},
        value=1
    ),
])


@app.callback(
    Output('main-graph', 'figure'),
    Input('select-data', 'value')
)
def update_graph(selected_data):
    fig = px.bar(df, x='date', y=selected_data, barmode='group')
    return fig


if __name__ == '__main__':
    # 서버 가동
    app.run_server(debug=True)
