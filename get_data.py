import yaml
import requests
from pathlib import Path

data_dir = Path("data")

if not data_dir.exists():
    data_dir.mkdir()

with open("data.yaml", "r") as f:
    data = yaml.load(f, Loader=yaml.FullLoader)

for entry in data:
    name = entry['name']
    url = entry['url']

    r = requests.get(url)
    path = data_dir / f"{name}.csv"

    with open(path, "w") as f:
        f.write(r.text)