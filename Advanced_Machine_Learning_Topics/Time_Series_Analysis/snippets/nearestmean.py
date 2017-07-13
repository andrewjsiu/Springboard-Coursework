
from random import randint

def test_idea(words_df):
    distances = []
    mean_words = words_df.groupby(words_df.index).mean()
    i = randint(0, words_df.shape[0])
    random_word = words_df.iloc[i]
    for mean_idx in range(mean_words.shape[0]):
        current_mean_word = mean_words.iloc[mean_idx]
        distances.append(DTWDistance(current_mean_word.values, random_word.values))
    return (random_word.name, distances)

word_type, distances = test_idea(words)
indexed_distances = enumerate(distances)
word_type
list(indexed_distances)