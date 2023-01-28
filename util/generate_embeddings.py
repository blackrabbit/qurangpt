import pandas as pd
import tiktoken

from openai.embeddings_utils import get_embedding
from numpy.lib.stride_tricks import sliding_window_view


embedding_model = "text-embedding-ada-002"
embedding_encoding = "cl100k_base"
max_tokens = 8191  

input_datapath = "../data/quran_english.csv" 
df = pd.read_csv(input_datapath)
print(df.columns)
df = df[["SrNo", "JuzNo", "SurahNo", "AyahNo", "EnglishTranslation"]]
df = df.dropna()

# Prefix ayats so we can find them later.
df['MarkedEnglishTranslation'] = '#' + df['SurahNo'].astype(str) + '.' + df['AyahNo'].astype(str) + '# ' +  df['EnglishTranslation']

surahs = df.groupby('SurahNo')
surahs_list = [surahs.get_group(x) for x in surahs.groups]

rolling_window_ayats = []
for surah in surahs_list:
    rolling_window_ayats.append(sliding_window_view(surah.MarkedEnglishTranslation, 3))

flattened_rolling_window_ayats = []
for surah in rolling_window_ayats:
    for rolling_ayats in surah:
        flattened_rolling_window_ayats.append(' '.join(rolling_ayats.tolist()))

df = pd.DataFrame(flattened_rolling_window_ayats, columns=['EnglishGroupAyats'])

encoding = tiktoken.get_encoding(embedding_encoding)
df["embedding"] = df.EnglishGroupAyats.apply(lambda x: get_embedding(x, engine=embedding_model))
df.to_csv("data/quran_english_rolling_window_size_3_with_embeddings.csv")