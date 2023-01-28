from flask import Flask, request, render_template, abort, jsonify
import pandas as pd
import numpy as np

from openai.embeddings_utils import get_embedding, cosine_similarity

app = Flask(__name__)

datafile_path = "data/quran_english_rolling_window_size_3_with_embeddings.csv"
df = pd.read_csv(datafile_path)
df["embedding"] = df.embedding.apply(eval).apply(np.array)

def query_model(df, query, n=3):
    query_embedding = get_embedding(
        query,
        engine="text-embedding-ada-002"
    )
    df["similarity"] = df.embedding.apply(lambda x: cosine_similarity(x, query_embedding))

    results = (
        df.sort_values("similarity", ascending=False)
        .head(n)
    )
    ayats = []
    for ayat in results.EnglishGroupAyats:
        ayats.append(ayat)

    return ayats

@app.route("/")
def index():
    return render_template('index.html')


@app.route('/search', methods=['GET'])
def search():
    q = request.args.get("q", default="", type=str)
    if q == "":
        abort(400)
    return jsonify(query_model(df, q))
    



