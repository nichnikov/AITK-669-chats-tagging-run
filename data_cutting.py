import os
import pandas as pd

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i: i + n]

'''
chats_ids = []
for num, df in enumerate(pd.read_csv(os.path.join(os.getcwd(), "data", "chats_20240420_20250420.csv"), chunksize=500000)):
    fn = "chats_20240420_20250420_" + str(num) + ".feather"
    # df.to_feather(os.path.join(os.getcwd(), "data", fn))
    chats_ids += df["chat_id"].unique().tolist()
    print(num, len(chats_ids))
    # print(num, "\n", df)

print(len(chats_ids))

chats_ids_df = pd.DataFrame([{"chat_id": cid} for cid in chats_ids])

print(chats_ids_df)

chats_ids_df.to_csv(os.path.join(os.getcwd(), "data", "chats_ids.csv"))'''

chats_ids_df = pd.read_csv(os.path.join(os.getcwd(), "data", "chats_ids.csv"))
print(chats_ids_df)
unique_chats_ids = chats_ids_df["chat_id"].unique()

k = 1
for chank_chats_ids in chunks(unique_chats_ids, 500000):
    chank_chats_ids_df = pd.DataFrame([{"chat_id": cid} for cid in chank_chats_ids])
    fn = "chank_chats_ids_" + str(k) + ".csv"
    chank_chats_ids_df.to_csv(os.path.join(os.getcwd(), "data", fn))
    k += 1