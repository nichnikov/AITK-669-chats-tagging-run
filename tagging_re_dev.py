import os
import re
import pandas as pd

df = pd.read_feather(os.path.join(os.getcwd(), "data", "tested_results_250331_4.feather"))

val_set = set(df["gpt_val"].to_list())
print(val_set)

res = []
for tx in val_set:
    r1 = re.sub(r"\n|\.|\d", " ", tx.lower())
    r2 = re.sub(r"\s+", " ", r1)
    r2_tuple = tuple([i for i in r2.split(" ") if i !=""])
    res.append(r2_tuple)

print(set(res))

for tp in res:
    if "да" not in tp and "нет" not in tp:
        print("""if "да" not in tp and "нет" not in tp:""", tp)