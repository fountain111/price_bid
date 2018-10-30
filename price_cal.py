'''
    -p :company bids will be sorted by number of [range].lenth, -p 1-300,2-400,,
    -o :outpu file ,csv format
    --help or -h: help

'''

import sys
import getopt
import numpy as np
import itertools
import pandas as pd
class Usage(Exception):
    def __init__(self,msg):
        self.msg = msg
        print(__doc__)

class Bid():

    def __init__(self,prices):
        self.prices_list = [list(map(int,str.split(value, '-')))
                            for value in str.split(prices, ',')]

        self.df = pd.DataFrame()

    def scores(self):
        #print(self.prices_list)
        price_list = []
        new_record = {}
        record_list = []
        prices_dict = {}
        for start,end in self.prices_list:
            price_list.append([value for value in range(start,end)])
        price_list = self._sort_in_list(price_list)

        for comb in itertools.product(*price_list):
            print('single_combination:',comb)
            mean = np.mean(comb)
            for key,price in enumerate(comb):
                if price > mean * 1.3:
                    #print('price>mean*130%:',price)
                    new_record['high_abnormal'] = price

                elif price < mean * 0.7:
                    #print('price>mean<70%:',price)
                    new_record['low_abnormal'] = price

                else:
                    prices_dict[key] = price
                    new_record['high_abnormal'] = None
                    new_record['low_abnormal'] = None

                new_record['index_' + str(key) + '_price'] = price
                #if price < 282:
                 #   print(new_record)
            high = max(prices_dict.values())
            low = min(prices_dict.values())
            for key, value in prices_dict.items():
                scores = ((high + low - value) / high) * 40
                new_record['index_'+str(key) + '_scores'] = scores
            new_record['high'] = high
            new_record['low'] = low
            #print(new_record)
            # new_record['high_abnormal'] = None
            # new_record['low_abnormal'] = None
            record_list.append(new_record)
            new_record = {}
            #print(record_list[0:1])
            #print(row)
        self.df = pd.DataFrame(record_list)
        #print(record_list[1])
        #print(self.df.head(5))
        return
    def to_csv(self,file_name):
        print('number of rows in file:',self.df.shape[0])
        self.df.to_csv(file_name)
    def _sort_in_list(self,price_list):
        #打牌那种插入法,比大小时,大的数向右滚动。
        for j,value in enumerate(price_list):
            if j <1:
                continue
            key = value
            i = j - 1
            while len(price_list[i])>len(key) and i >=0:
                price_list[i+1] =  price_list[i]
                i-=1
            price_list[i+1] = key

        print('sorted price range:',price_list)
        return price_list
def main(argv=None):
    if argv is None:
        argv=sys.argv
    try:
        try:
            opts,args = getopt.getopt(argv[1:],'hp:o:',['help'])
        except getopt.error as err:
            raise Usage(err)
        if len(opts)==0:
            raise Usage('opts empty')

        for o, a in opts:
            if o in ('-h', '--help'):
                raise Usage('user-help')
            if o =='-p':
                bid = Bid(a)
                bid.scores()
            if o in ('-o'):
                bid.to_csv(a)

    except Usage as e:
        print(e.msg)
        return 2


if __name__ == '__main__':
    sys.exit(main())