from pathlib import Path
import json

import options

def _addfile(path: Path, collection: dict | list):
    if isinstance(collection, dict):
        collection[path.name] = None
    if isinstance(collection, list):
        collection.append(path.name)

def _adddir(path: Path, collection: dict | list):
    if isinstance(collection, dict):
        key = path.name or '.' 
        collection[key] = {}
        return collection[key]
    
    if isinstance(collection, list):
        key = path.name or '.'
        d = {key:[]}
        collection.append(d)
        return d[key]

def path_to_collection(path:Path, l:list, *exclude: str, level=0) -> list:
    if isinstance(path, str):
        path = Path(path)
    if path.name in exclude:
        return
    if not path.exists():
        raise FileNotFoundError(f'path {path.resolve().as_posix()} not found')
    if path.is_file():
        _addfile(path, l)
    if path.is_dir():
        element = _adddir(path, l)
        for p in path.glob('*'):
            path_to_collection(p, element, *exclude, level=level+1)
    if level == 0:
        return l

def save_jsonpaths(jsonpath: str, root:str|Path, *exclude: str, use_dict=True) -> None:
    collection = {} if use_dict else []
    print(f'{collection = }')
    collection = path_to_collection(root, collection, *exclude)
    with open(jsonpath, 'w') as jfp:
        json.dump(collection, jfp, indent=2)

def load_jsonpaths(jsonpath: str) -> list | dict:
    with open(jsonpath) as jfp:
        collection = json.load(jfp)
    return collection

if __name__ == '__main__':
    args = options.parse()
    save_jsonpaths(args.jsonpath, args.path, *args.exclude, use_dict=args.dict)
    print(json.dumps(load_jsonpaths(args.jsonpath), indent=2))
