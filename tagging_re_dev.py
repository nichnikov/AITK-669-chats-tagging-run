import os
import re
import pandas as pd

df = pd.read_feather(os.path.join(os.getcwd(), "data", "tested_results_250331_4.feather"))

val_set = set(df["gpt_val"].to_list())
print(val_set)
handled_examples = ['блабла, да', 'всякая белиберда нето дането 1. Нет  \n2. Нет', 'Rate-limit error', '1. Нет\n всякая белиберда нето дането 2. Нет', ' всякая белиберда нето дането 1. Да.\nвсякая белиберда нето дането 2. всякая белиберда нето данетоДа.', 'всякая белиберда нето дането 1. Нет  всякая белиберда нето дането \nвсякая белиберда нето дането 2.всякая белиберда нето дането  Да']

val_list = list(val_set) + handled_examples

res = []
for tx in val_list:
    r1 = re.sub(r"[^а-я]", " ", tx.lower())
    r2 = re.sub(r"\s+", " ", r1)
    r3 = re.findall(r"\bда\b|\bнет\b", r2)
    if r3:
        print(r2, r3)
        res.append(tuple(r3))
    else:
        print(tx, ["err"])
        res.append(tuple(["err"]))


print(set(res))
