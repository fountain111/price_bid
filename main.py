
import numpy as np
import pandas as pd
def main():
    new_record = {}
    hc_bid_dict = {'hc':tuple(i*10000 for i in range(400,470))}
    hc_price_list =hc_bid_dict.values()
    others = {'c1':tuple( i*10000 for i in range(100,470)),'c2':(4664000,),'c3':(4685200,)}

    prices_dict={}


    record_list = []

    # 最少的tuple放在最外层,最多的tuple放在最里面,保证每一个组合都被遍历到。
    for j in others['c2']:
        for k in others['c3']:
            for l in hc_bid_dict['hc']:
                for m in others['c1']:
                    mean = np.mean([j,k,m,l])
                    #print(mean)
                    for key,price in {'hc':l,'c1':m,'c2':j,'c3':k}.items():
                        if price >mean*1.3:
                            #print(price)
                            new_record['high_abnormal'] = price
                        elif price < mean * 0.7:
                            new_record['low_abnormal'] = price
                        else:
                            prices_dict[key]=price
                            new_record['high_abnormal'] = None
                            new_record['low_abnormal'] = None
                            new_record[key+'price'] = price



                    high = max(prices_dict.values())
                    low = min(prices_dict.values())
                    for key,value in prices_dict.items():
                        scores = ((high + low - value)/high)*40
                        new_record[key+'scores'] = scores
                    new_record['high'] = high
                    new_record['low'] = low
                    #print(new_record)
                    #new_record['high_abnormal'] = None
                    #new_record['low_abnormal'] = None
                    if (new_record['high_abnormal']!=None):
                        record_list.append(new_record)

                    else:
                        #print(new_record)
                        continue

    #df = pd.DataFrame(record_list)
    #print(df[df['high_abnormal']!=0])
    #df.to_csv('./scores.csv')
    #print(df.shape)
    print(len(record_list))


            #print('和分数:',u_bid,u_value,'鸿程报价和分数:',hc_bid,hc_value)

    # 忽略别家的报价比我司高的情况,
if __name__ == '__main__':
    main()
