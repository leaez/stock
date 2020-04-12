

import easyquotation

def test_quotation():
    quotation = easyquotation.use('sina') # 新浪 ['sina'] 腾讯 ['tencent', 'qq'] 

    ## only last day data: 
    #dt = quotation.market_snapshot(prefix=True) # 获取所有股票行情 prefix  是否带 sz/sh 
    
    #quotation.real('162411') # 支持直接指定前缀，如 'sh000001'
    #quotation.stocks(['000001', '162411'])  #多只股票
    
    dt = quotation.stocks(['sh000001', 'sz000001'], prefix=True) # 同时获取指数和行情
    print(dt);

def test_daykline():
    quotation  = easyquotation.use("daykline")
    #data = quotation.real(['00001','00700'])
    #data = quotation.stocks('sh000001', prefix=True)

    print(data )
    #print(data['sh000001'][-1] )
    #print(data)


#test_daykline()
test_quotation()
print("end!")
'''
aaa
'''
        
