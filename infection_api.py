import pandas as pd
import requests
import xmltodict
import json


# url, service key 정의
URL = 'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19InfStateJson'
SERVICE_KEY = 'sroGJkpLtL0m51Oc6IcQ+zLwySx/2Mx5uXtFRHJCB+7gnPwa5P9bwZkmqztNvhR8k3ezJb8wNOqOthswit7mFA=='

# 시작날짜, 끝날짜 정의
startCreateDt = 20200101
endCreateDt = 20211101

# 파라미터 설정
query_params = {
    'ServiceKey': SERVICE_KEY,
    'startCreateDt': startCreateDt,
    'endCreateDt': endCreateDt
}

# load datasets
req = requests.get(URL, params=query_params)    # API 호출

# xml 데이터 dict 변환
req = xmltodict.parse(req.text)     # xml
src_data = json.loads(json.dumps(req))      # json 파일로 변경

# DataFrame 정리
temp = src_data['response']['body']['items']['item']     # 필요 데이터 파싱
data = pd.DataFrame(temp)        # DataFrame 변환

# save datasets
data.to_csv('data.csv')
