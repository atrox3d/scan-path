from pathlib import Path
import json

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

def scan(path:Path, collection: dict|list, *exclude: str, level=0) -> dict|list:
    if isinstance(path, str):
        path = Path(path)
    if path.name in exclude:
        return collection
    if not path.exists():
        raise FileNotFoundError(f'path {path.resolve().as_posix()} not found')
    if path.is_file():
        _addfile(path, collection)
    if path.is_dir():
        element = _adddir(path, collection)
        for p in path.glob('*'):
            scan(p, element, *exclude, level=level+1)
    if level == 0:
        return collection

def save_jsonpaths(jsonpath: str, root:str|Path, *exclude: str, use_dict=True) -> None:
    collection = {} if use_dict else []
    print(f'{collection = }')
    collection = scan(root, collection, *exclude)
    with open(jsonpath, 'w') as jfp:
        json.dump(collection, jfp, indent=2)

def load_jsonpaths(jsonpath: str) -> list | dict:
    with open(jsonpath) as jfp:
        collection = json.load(jfp)
    return collection

