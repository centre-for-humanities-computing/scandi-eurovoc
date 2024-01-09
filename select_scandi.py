import glob
import gzip
import json

from tqdm import tqdm

skipped = []
records = []
files = glob.glob("Eurovoc/files/*.jsonl.gz")
for file in tqdm(files, desc="Going through all files."):
    with gzip.open(file) as in_file:
        for line in in_file:
            try:
                record = json.loads(line)
                if record["lang"] in ["dan", "swe"]:
                    records.append(record)
            except TypeError:
                skipped.append(line)

with open("scandi_eurovoc.jsonl", "w") as out_file:
    for record in records:
        out_file.write(json.dumps(record) + "\n")

with open("skipped.txt", "w") as out_file:
    out_file.writelines(skipped)
