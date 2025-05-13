import os, json, datetime

def load_json_fixture(filename):
    base_dir = os.path.dirname(__file__)
    file_path = os.path.join(base_dir, '..', 'fixtures', filename)

    with open(file_path, encoding='utf-8') as f:
        return json.load(f)


def parse_date_fields(data, date_keys):
    for item in data:
        for key in date_keys:
            if key in item and isinstance(item[key], str):
                item[key] = datetime.datetime.strptime(item[key], "%Y-%m-%d").date()
    return data
