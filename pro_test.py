import tushare as ts
import time
from datetime import datetime

print(ts.__version__)
pro = ts.pro_api()

# 
def get_daily( ts_code='', trade_date='', start_date='', end_date=''):
    for _ in range(3):
        try:
            if trade_date:
                df = pro.daily(ts_code=ts_code, trade_date=trade_date)
            else:
                df = pro.daily(ts_code=ts_code, start_date=start_date, end_date=end_date)
        except:
            time.sleep(1)
        else:
            return df


def get_date(exchange='SSE', start_date='20200101', end_date='20200401'):
    df = pro.trade_cal(exchange='SSE', is_open='1', start_date='20200101', end_date='20200401', 
        fields='cal_date') 
    for date in df['cal_date'].values:
        print(date)
    return df['cal_date'].values

#df = ts.get_hist_data('600848')
#df = ts.get_hist_data('600848',start='2020-02-25',end='2017-10-25')

def get_grade():
    pct_change_arr = get_daily(trade_date='20180810')

    changesP = [0,0,0,0,0,0,0,0,0,0,0,0]
    changesN = [0,0,0,0,0,0,0,0,0,0,0,0]
    for c in pct_change_arr['pct_chg']:
        if   c == -10:          changesN[11]+=1; 
        elif c>-10 and c<=-9:   changesN[10]+=1;
        elif c>-9 and c<=-8:    changesN[9]+=1;
        elif c>-8 and c<=-7:    changesN[8]+=1;
        elif c>-7 and c<=-6:    changesN[7]+=1;
        elif c>-6 and c<=-5:    changesN[6]+=1;
        elif c>-5 and c<=-4:    changesN[5]+=1;
        elif c>-4 and c<=-3:    changesN[4]+=1;
        elif c>-3 and c<=-2:    changesN[3]+=1;
        elif c>-2 and c<=-1:    changesN[2]+=1;
        elif c>-1 and c<0:      changesN[1]+=1;
        if c == 0:              changesP[0]+=1; 
        elif c>0 and c<=1:      changesP[1]+=1;
        elif c>1 and c<=2:      changesP[2]+=1;
        elif c>2 and c<=3:      changesP[3]+=1;
        elif c>3 and c<=4:      changesP[4]+=1;
        elif c>4 and c<=5:      changesP[5]+=1;
        elif c>5 and c<=6:      changesP[6]+=1;
        elif c>6 and c<=7:      changesP[7]+=1;
        elif c>7 and c<=8:      changesP[8]+=1;
        elif c>8 and c<=9:      changesP[9]+=1;
        elif c>9 and c<10:      changesP[10]+=1;
        elif c==10:             changesP[11]+=1;
    print( changesP)
    print( changesN)
    return [changesP,changesN]

#dt = datetime(2018, 1, 1)
dt = get_date();
print(type(1+ int(dt[0])))

