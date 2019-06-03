
조선해양공학과 / 201529168 / 이준하

과제명 : 수출입실적 검색및 판다스출력

## 프로젝트 개요
세관의 항구 항만 수출입자료를 통해 2001년도부터 2018년도까지의 각 항구 항만별 수출입자료를 인덱싱하여 판다스로 출력해낸다.

## 사용한 공공데이터 
[데이터보기](https://github.com/garugon12/python-work/blob/master/%ED%95%AD%EA%B5%AC%ED%95%AD%EB%A7%8C%EC%88%98%EC%B6%9C%EC%9E%85%EC%8B%A4%EC%A0%81.csv)

## 소스
* [링크로 소스 내용 보기](https://github.com/garugon12/python-work/blob/master/%EA%B8%B0%EB%A7%90%EA%B3%BC%EC%A0%9C.py) 

import pandas as pd
df=pd.read_csv('항구항만수출입실적.csv',engine='python')

timelist = sorted(list(set(df['기간'])))
regionlist = sorted(list(set(df['항구공항명'])))

while True :

    mode = input("모드를 입력하세요(1:기간리스트 2:항구공항명리스트 3:검색모드 q:종료)")

    if int(mode) in range(1,4) :
        mode=int(mode)

    elif mode == 'q' :
        break

    else :
        print("잘못된 모드입력")
        continue

    if mode == 1 :
        print(timelist)
        continue

    if mode == 2 :
        print(regionlist)
        continue

    if mode == 3 :
        while True :

            time = input('기간을 입력하세요(q입력시 검색모드종료)')
            region = input('항구(공항)위치를 입력하세요(q입력시 검색모드종료)')

            if time == "" or region == "" :

                if time == "" and region == "":
                    print("기간또는 항구위치 둘중 하나는 입력해야합니다.")
                    continue

                if time == "" and region in regionlist :
                    df1 = df.loc[df['항구공항명'] == region]
                    print(df1)
                    continue

                if region == "" and time in timelist :
                    df1 = df.loc[df['기간'] == time]
                    print(df1)
                    continue

                if time not in timelist :
                    print("기간이 잘못되었습니다.")
                    continue

                if time not in regionlist :
                    print("항구공항명이 잘못되었습니다.")
                    continue

            elif region == 'q' or time == 'q' :
                    print("검색모드를 종료합니다.")
                    break

            elif time not in timelist or region not in regionlist :

                if time not in timelist and region not in regionlist :
                    print("기간과 항구공항명이 잘못되었습니다.")

                if time not in timelist :
                    print("기간이 잘못되었습니다.")
                    continue

                if time not in regionlist :
                    print("항구공항명 기간에 없거나이 잘못되었습니다.")
                    continue

            else :
                df1 = df.loc[df['기간']==time]
                df2 = df1.loc[df['항구공항명']==region]
                print(df2)
