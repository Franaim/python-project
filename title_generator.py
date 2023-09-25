import random

# Lists of nouns and adjectives to generate the artwork title
nouns = ["aurora", "object", "panorama", "elixir", "chair", "mirror", "facade", "phenomenon", "resonance", "memento", "artifact"]
adjectives1 = ["enigmatic", "expressive", "dynamic", "political", "honest", "provocative", "real", "cruel", "truthful", "world's"]
adjectives2 = ["ivory", "cerulean", "golden", "indigo", "unique", "Japanese", "Maltese", "Eastern", "Western", "southern", "blood-red", "dystopian"]


# This function is then imported into the run.py file
def generate_string(num_words):
    """
    Based on the number entered by the user, it generates random strings from the lists of nouns and adjetives.
    """
    title_words = []
    adjectives_lists = [adjectives1, adjectives2]
    # Since a title typically always includes a noun, we need to generate one less adjective than the total number of words entered by the user
    number_of_adjectives = num_words - 1
    for n in range(number_of_adjectives):
        # First we take and adjective and append it to the empty list title_words, taking one from each list in case there are two of them and, by using the pop method, only from the adjectives2 list if it's one
        title_words.append(random.choice(adjectives_lists.pop()))
    # Then we take a noun randomly from the nouns list and we append it to the title_words list
    title_words.append(random.choice(nouns))
    # Now we return a string using the join method adding spaces between the words and capitalizing it
    return ' '.join(title_words).capitalize()
    