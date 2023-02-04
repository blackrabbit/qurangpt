![logo](https://github.com/blackrabbit/qurangpt/blob/main/docs/logo.png?raw=true)

# QuranGPT

This is a text embedding model using the OpenAI API to generate an embedding and then use it to do a semantic search through the quran.

The original source of the English translation of the quran can be downloaded from [here](https://drive.google.com/file/d/13gCvW0hHyQGvYSqXP71pgD2LNOvtb8Gi/view?usp=sharing).

It is deployed at https://qurangpt.dev


## Run

NOTE: You must have your own OpenAI key to use this. You can create an account with a free trial on their website.

1. Create a new virtual environment for the project
2. Install the `requirements.txt` into that venv.
3. Create a directory in the root named `data/`.
4. Copy the source quran text into that directory from [here](https://drive.google.com/file/d/13gCvW0hHyQGvYSqXP71pgD2LNOvtb8Gi/view?usp=sharing).
5. Run `python generate_embeddings.py`
6. After that finishes running, you should now be able to run `search.py`.

## Examples

Query: 'is alcohol allowed in islam?'
```
#5.90# O ye who believe! Intoxicants and gambling, (dedication of) stones, and (divination by) arrows, are an abomination,- of Satan's handwork: eschew such (abomination), that ye may prosper. #5.91# Satan's plan is (but) to excite enmity and hatred between you, with intoxicants and gambling, and hinder you from the remembrance of Allah, and from prayer: will ye not then abstain? #5.92# Obey Allah, and obey the Messenger, and beware (of evil): if ye do turn back, know ye that it is Our Messenger's duty to proclaim (the message) in the clearest manner.
#37.45# Round will be passed to them a Cup from a clear-flowing fountain, #37.46# Crystal-white, of a taste delicious to those who drink (thereof), #37.47# Free from headiness; nor will they suffer intoxication therefrom.
#56.17# Round about them will (serve) youths of perpetual (freshness), #56.18# With goblets, (shining) beakers, and cups (filled) out of clear-flowing fountains: #56.19# No after-ache will they receive therefrom, nor will they suffer intoxication:
```
