def compute_bag_of_words(corpus: list) -> list[str]:
    '''Returns a list of unique words from the corpus
    
    Args:
        corpus: list of the sentences
    
        Returns: list of unique words from the corpus
    '''
    bag_of_words = []

    for sentence in corpus:
        words = sentence.split(' ')

        for word in words:
            if word not in bag_of_words:
                bag_of_words.append(word)

    bag_of_words = sorted(bag_of_words)

    return bag_of_words


def tokenize(txt: str) -> list:
    '''Converts a sentence txt to a vector
    
    Args:
        txt: a sentence to be tokenized

    Returns:
        vector: a list of numbers representing the sentence
    '''

    corpus = [
        "Tôi thích môn Toán",
        "Tôi thích AI",
        "Tôi thích âm nhạc"
    ]

    # Compute the bag_of_words
    bag_of_words = compute_bag_of_words(corpus)
    
    # Initialize a vector
    vector = [0 for _ in range(len(bag_of_words))]

    # Loop through each word in txt to generate a vector
    for word in txt.split(' '):
        index = bag_of_words.index(word)
        
        # Update occurrences of word in vector
        vector[index] += 1

    return vector

tokenize('Tôi thích AI thích Toán')


assert tokenize('Tôi thích AI thích Toán') == [1, 1, 1, 0, 0, 2, 0]
print('Unit test passed')