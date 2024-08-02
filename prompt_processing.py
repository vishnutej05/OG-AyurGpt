
def tokenizer(content):
    cw = ["A", "a", "the", "and", "of", "to", "in", "is", "you", "that","pain","have", "it", "he", "she", "we", "they", "i", "my","am", "for", "was", "on", "with", "as", "by", "at", "but", "not", "from", "or", "an", "if", "this", "all", "have", "one", "can", "will", "would", "about", "there", "out", "up", "so", "what", "when", "how", "which", "who", "get", "go", "me", "him", "her", "his", "its", "our", "your", "their", "my", "no", "do", "are", "were", "been", "into", "more", "time", "can't", "should", "could", "did", "has", "had", "may", "might", "must", "shall", "should", "us", "them", "before", "after", "over", "under", "between", "through", "because", "why", "now", "then", "still", "just", "too", "down", "also", "well", "here", "back", "only", "even", "very", "good", "first", "new", "way", "want", "give", "day", "most", "work", "make", "know", "see", "come", "take", "need", "use", "feel", "try", "call", "should", "turn", "long", "great", "little", "own", "right", "place", "house", "man", "old", "year", "last", "people", "part", "tell", "point", "case", "week", "company", "number", "fact", "question", "point", "group", "fact", "question", "point", "group", "world", "different", "example", "hand", "small", "large", "place", "turn", "right", "big", "high", "start", "same", "part", "good", "line", "seem", "hand", "keep", "house", "place", "line", "name", "night", "run", "move", "live", "year", "place", "try", "home", "life", "case", "side", "name", "world", "end", "keep", "look", "use", "own", "same", "home", "work", "look", "part", "place", "try", "case", "hand", "place", "line", "move", "name", "part", "point", "right", "same", "work", "end", "feel", "keep", "live", "look", "make", "own", "place", "try", "use", "world", "year", "people", "find", "house", "line", "name", "place", "work", "live", "people", "right", "case", "home", "end", "life", "look", "name", "part", "people", "right", "world", "back", "end", "hand", "home", "name", "people", "work", "life", "look", "place", "end",
          "home", "life", "line", "people", "place", "work", "point", "right", "side", "use", "work", "day", "end", "home", "house", "life", "part", "point", "week", "work", "hand", "life", "place", "part", "try", "week", "year", "end", "hand", "life", "line", "part", "place", "point", "side", "week", "work", "year", "back", "end", "house", "line", "look", "place", "world", "year", "life", "part", "people", "place", "right", "year", "line", "point", "work", "place", "work", "house", "line", "look", "make", "place", "try", "work", "life", "look", "place", "point", "week", "work", "day", "hand", "line", "look", "place", "year", "work", "people", "line", "work", "year", "end", "life", "name", "place", "world", "work", "life", "name", "place", "year", "people", "world", "year", "line", "point", "right", "work", "year", "end", "life", "place", "people", "week", "hand", "home", "life", "look", "part", "week", "year", "back", "end", "home", "house", "line", "place", "world", "year", "life", "part", "people", "place", "right", "year", "line", "point", "work", "place", "work", "house", "line", "look", "make", "place", "try", "work", "life", "look", "place", "point", "week", "work", "day", "hand", "line", "look", "place", "year", "work", "people", "line", "work", "year", "end", "life", "name", "place", "world", "work", "life", "name", "place", "year", "people", "world", "year", "line", "point", "right", "work", "year", "end", "life", "place", "people", "week", "hand", "home", "life", "look", "part", "week", "year", "back", "end", "home", "house", "line", "place", "world", "year", "life", "part", "people", "place", "right", "year", "line", "point", "work", "place", "work", "house", "line", "look", "make", "place", "try", "work", "life", "look", "place", "point", "week", "work", "day", "hand", "line", "look", "place", "year", "work", "people", "line", "work", "year", "end", "life", "name", "place", "world", "work", "life", "name", "place", "year", "people", "world", "year", "line"]
    

    content = content.lower()
    content = content.replace(",", " ")
    content = content.replace(".", " ")
    content = content.replace("!", " ")
    content = content.replace("?", " ")
    tokens = content.split(" ")
    tokens = set(tokens)
    tokens = list(tokens)
    if '' in tokens:
        tokens.remove('')
    n_tokens = []
    indices=[]
    for token in tokens:
        if token in cw:
            indices.append(token)
    for i in indices:
        tokens.remove(i)
    return tokens
