import json

from datasets import Dataset


def generate_lines():
    with open("scandi_eurovoc.jsonl") as in_file:
        for line in in_file:
            yield json.loads(line.strip())


ds = Dataset.from_generator(generate_lines)
ds = ds.shuffle(seed=42)
ds = ds.train_test_split(test_size=0.2, seed=42)
ds.push_to_hub("kardosdrur/scandi_eurovoc")
