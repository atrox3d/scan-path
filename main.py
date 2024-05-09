import json

import options
import scan

if __name__ == '__main__':
    args = options.parse()
    scan.save_jsonpaths(args.jsonpath, args.path, *args.exclude, use_dict=args.dict)
    print(json.dumps(scan.load_jsonpaths(args.jsonpath), indent=2))
