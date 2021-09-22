# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd


# 시트 스타일 선택
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# 앱 설정
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# 데이터 생성
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

# 바 그래프 생성
fig = px.bar(df, x='Fruit', y='Amount', color='City', barmode='group')

# 레이아웃 설정
app.layout = html.Div(children=[
    # 제목 배치
    html.H1(children='Hello Dash'),
    # 텍스트 배치
    html.Div(children='''
        Dash: A web application framework for Python.
    '''),
    # 그래프 배치
    dcc.Graph(
        id='example-graph',
        figure=fig      # 보여줄 그래프 설정
    )
])


if __name__ == '__main__':
    # 서버 가동
    app.run_server(debug=True)
