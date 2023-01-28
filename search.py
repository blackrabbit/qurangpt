import pandas as pd
import numpy as np

from openai.embeddings_utils import get_embedding, cosine_similarity


datafile_path = "data/quran_english_rolling_window_size_3_with_embeddings.csv"
df = pd.read_csv(datafile_path)
df["embedding"] = df.embedding.apply(eval).apply(np.array)

# search through the reviews for a specific product
def search(df, query, n=3, pprint=True):
    query_embedding = get_embedding(
        query,
        engine="text-embedding-ada-002"
    )
    df["similarity"] = df.embedding.apply(lambda x: cosine_similarity(x, query_embedding))

    results = (
        df.sort_values("similarity", ascending=False)
        .head(n)
    )
    return results


results = search(df, "is jesus viewed favorably in islam", n=3)
for ayat in results.EnglishGroupAyats:
    print(ayat)
