# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_html_components as html
import pandas as pd


# 데이터 로드
df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/'
                 'c78bf172206ce24f77d6363a2d754b59/raw/c353e8ef842413cae56ae3920b8fd78468aa4cb2/'
                 'usa-agricultural-exports-2011.csv')


# 대시보드에 테이블 생성
def generate_table(dataframe, max_rows=10):
    return html.Table([
        # 테이블 헤드 생성
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        # 테이블 바디 생성
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])


# 시트 스타일 선택
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# 앱 설정
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# 레이아웃 설정
app.layout = html.Div(children=[
    html.H4(children='US Agriculture Exports (2011)'),
    generate_table(df)      # 테이블 생성
])

if __name__ == '__main__':
    # 서버 가동
    app.run_server(debug=True)
