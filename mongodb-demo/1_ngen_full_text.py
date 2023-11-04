import json

with open("jobs.json", "r") as file:
    data = json.load(file)


def flatten_dict(d, parent_key="", sep=" "):
    items = []
    for k, v in d.items():
        if k == "deadline" or k == "price":
            pass
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        elif isinstance(v, list):
            items.append((new_key, ", ".join(map(str, v))))
        else:
            items.append((new_key, v))
    return dict(items)


for item in data:
    flat_item = flatten_dict(item)
    full_text = "; ".join([f"{key} is '{value}'" for key, value in flat_item.items()])
    item["full_text"] = full_text

with open("jobs_full.json", "w") as file:
    json.dump(data, file, indent=4)
