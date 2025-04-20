import re
import datetime
import uuid
import json
import os

def parse_iso_date(date_str: str) -> datetime.datetime:
    dt = datetime.datetime.fromisoformat(date_str)
    return dt

def format_date_pretty(dt: datetime.datetime) -> str:
    return dt.strftime("%B %d, %Y at %H:%M:%S")

def calculate_age(birthdate: str) -> int:
    dob = parse_iso_date(birthdate)
    today = datetime.datetime.now()
    return today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

def is_palindrome(s: str) -> bool:
    cleaned = re.sub(r'[^A-Za-z0-9]', '', s).lower()
    return cleaned == cleaned[::-1]

def count_vowels(s: str) -> int:
    return sum(1 for ch in s.lower() if ch in "aeiou")

def reverse_words(sentence: str) -> str:
    return " ".join(sentence.split()[::-1])

def slugify(text: str) -> str:
    normalized = re.sub(r'\W+', '-', text.lower()).strip('-')
    return normalized

def merge_dicts(dicts: list[dict]) -> dict:
    result = {}
    for d in dicts:
        result.update(d)
    return result

def flatten_list(nested: list) -> list:
    flat = []
    for item in nested:
        if isinstance(item, list):
            flat.extend(flatten_list(item))
        else:
            flat.append(item)
    return flat

def generate_uuid() -> str:
    return str(uuid.uuid4())

def read_json_file(path: str) -> dict:
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def write_json_file(data: dict, path: str):
    dirpath = os.path.dirname(path)
    if dirpath and not os.path.exists(dirpath):
        os.makedirs(dirpath)
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)

def list_files(directory: str, ext: str = "") -> list:
    files = []
    for root, _, filenames in os.walk(directory):
        for fn in filenames:
            if not ext or fn.endswith(ext):
                files.append(os.path.join(root, fn))
    return files

def load_env_vars(filepath: str) -> dict:
    env = {}
    with open(filepath) as f:
        for line in f:
            if "=" in line and not line.startswith('#'):
                key, val = line.strip().split('=', 1)
                env[key] = val
    return env

def chunk_list(items: list, size: int) -> list:
    return [items[i:i+size] for i in range(0, len(items), size)]

def safe_divide(a: float, b: float) -> float:
    return a / b if b != 0 else float('inf')

def timestamp_to_unix(dt: datetime.datetime) -> int:
    return int(dt.timestamp())

def unix_to_datetime(ts: int) -> datetime.datetime:
    return datetime.datetime.fromtimestamp(ts)

def ensure_dir(path: str):
    if not os.path.exists(path):
        os.makedirs(path)

def dict_diff(a: dict, b: dict) -> dict:
    diff = {}
    for k in set(a) | set(b):
        if a.get(k) != b.get(k):
            diff[k] = {'old': a.get(k), 'new': b.get(k)}
    return diff