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

# 마크다운 텍스트
markdown_text = '''
### Dash and Markdown

Dash apps can be written in Markdown.
Dash uses the [CommonMark](http://commonmark.org/)
specification of Markdown.
Check out their [60 Second Markdown Tutorial](http://commonmark.org/help/)
if this is your first introduction to Markdown!
'''


# 데이터 로드
df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/'
                 '5d1ea79569ed194d432e56108a04d188/raw/a9f9e8076b837d541398e999dcbac2b2826a81f8/gdp-life-exp-2007.csv')

# 버블차트 생성
fig = px.scatter(df, x="gdp per capita", y="life expectancy",
                 size="population", color="continent", hover_name="country",
                 log_x=True, size_max=60)

# 레이아웃 설정
app.layout = html.Div([
    # 마크다운 배치
    dcc.Markdown(children=markdown_text),
    # 그래프 배치
    dcc.Graph(
        id='life-exp-vs-gdp',
        figure=fig
    )
])


if __name__ == '__main__':
    # 서버 가동
    app.run_server(debug=True)
