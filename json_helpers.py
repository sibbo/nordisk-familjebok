import json

# Get entries from json file
def read_items(filename: str) -> list[dict]:
    with open(f"{filename}.json", 'r', encoding='utf-8') as infile:
        items = json.loads(infile.read())
    return items

# Write entries to json file
def write_items(items: list[dict], filename: str) -> None:
    with open(f"{filename}.json", 'w', encoding='utf-8') as outfile:
        json.dump(items, outfile, ensure_ascii=False, indent=4)