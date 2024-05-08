import argparse

def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--dict', action='store_true', default=True)
    parser.add_argument('-l', '--list', action='store_true', default=False)
    parser.add_argument('-e', '--exclude', action='append', default=['.git'])
    parser.add_argument('-p', '--path', default='.')
    parser.add_argument('-j', '--jsonpath', default='maze-solver.json')
    
    args = parser.parse_args()
    args.dict = not args.list
    print(args)
    return args
