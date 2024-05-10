import argparse

def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--dict', action='store_true', default=True)
    parser.add_argument('-l', '--list', action='store_true', default=False)
    parser.add_argument('-e', '--exclude', action='append', default=['.git', '__pycache__'])
    parser.add_argument('-p', '--path', default='.')
    parser.add_argument('-i', '--indent', type=int, default=2)
    parser.add_argument('-j', '--jsonpath', default='scan-path.json')
    
    args = parser.parse_args()
    args.dict = not args.list
    return args
