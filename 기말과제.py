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