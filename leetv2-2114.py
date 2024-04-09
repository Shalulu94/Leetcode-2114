sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]

# Kept getting an error when testing my solution in Leetcode. 
# Unsure whether it's to do with my code formatting when submitting
# Have tested it myself and below code works

# This is the revised solution which is dynamic enough to address any number of total sentences

def sentence_words():
    word_sentence = []

    for sentence in sentences:
        word_count = 1
        for words in sentence:
            if words == " ":
                word_count += 1
        word_sentence.append(word_count)

    word_sentence.sort(reverse=True)
    return(word_sentence[0])


print(sentence_words())


