import json

import options
import tree

if __name__ == '__main__':
    args = options.parse()
    print(args)
    tree.save_jsonpaths(args.jsonpath, args.path, *args.exclude, use_dict=args.dict)
    print(json.dumps(tree.load_jsonpaths(args.jsonpath), indent=args.indent))
