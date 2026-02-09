import os 
import json
import math

n = 5

json_files = os.listdir("jsons")

for file in json_files:
    with open(f"jsons/{file}", "r", encoding="utf-8") as f:
        data = json.load(f)

        new_chunks = []
        num_chunks = len(data["chunks"])
        num_groups = math.ceil(num_chunks/n)

        for i in range(num_groups):
            start_idx = (i*n)
            end_idx = min((i+1)*n, num_chunks)
            

            chunk_group = data["chunks"][start_idx:end_idx]

            new_chunks.append(
                {
                    "title": chunk_group[0]["title"],
                    "start": chunk_group[0]["start"],
                    "end": chunk_group[-1]["end"],
                    "text": "".join([chunk_group[c]["text"] for c in range(len(chunk_group))])
                }
            )
        data["chunks"] = new_chunks

        os.makedirs("newjsons", exist_ok=True)
        with open(os.path.join("newjsons", file), "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4)
    

print("Done with all JSON files !! Check 'newjsons' ")
