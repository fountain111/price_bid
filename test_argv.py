'''
    -t :test
'''

import sys
import getopt

class Usage(Exception):
    def __init__(self,msg):
        self.msg = msg
class Problem():

def main(argv=None):
    if argv is None:
        argv=sys.argv
    try:
        try:
            opts,args = getopt.getopt(argv[1:],'h',['help'])
        except getopt.error as err:
            raise Usage(err)
        for o, a in opts:
            if o in ('-h', '--help'):
                print(__doc__)
                sys.exit(0)
    except Usage as e:
        print(e.msg)
        print('for help use --help')
        return 2


if __name__ == '__main__':
    sys.exit(main())