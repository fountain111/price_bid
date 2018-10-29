'''
    -p :company bids-p 1-300,2-400
    --help or -h: help

'''

import sys
import getopt
import numpy as np
class Usage(Exception):
    def __init__(self,msg):
        self.msg = msg
        print(__doc__)

class Bid():

    def __init__(self,prices):
        self.prices_list = [list(map(int,str.split(value, '-')))
                            for value in str.split(prices, ',')]

        print(self.prices_list)

    def scores(self):
        print(self.prices_list)
        price_list = []
        mean = 0
        for start,end in self.prices_list:
            price_list.append([value*10000 for value in range(start,end)])
        price_list = self._sort_in_list(price_list)

        return

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

        #print(price_list)
def main(argv=None):
    if argv is None:
        argv=sys.argv
    try:
        try:
            opts,args = getopt.getopt(argv[1:],'hp:',['help'])
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

    except Usage as e:
        print(e.msg)
        return 2


if __name__ == '__main__':
    sys.exit(main())