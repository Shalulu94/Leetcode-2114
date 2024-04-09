# This was my first iteration. Provided the correct answer however was not dynamic enough to respond to more than 3 sentences.
# Answered the question, but would not work for any entries where sentences[i] > 3

sentences = ["please wait", "continue to fight", "continue to win"]

index = len(sentences)

sentence1 = sentences[0]
sentence2 = sentences[1]
sentence3 = sentences[2]

# sentence1_wordcount = 1
# sentence2_wordcount = 1
# sentence3_wordcount = 1

def sentence_words1():
    sentence1_wordcount = 1

    for words in sentence1:
        if words == " ":
            sentence1_wordcount += 1
    return(sentence1_wordcount)

def sentence_words2():
    sentence2_wordcount = 1

    for words in sentence2:
        if words == " ":
            sentence2_wordcount += 1
    return(sentence2_wordcount)

def sentence_words3():
    sentence3_wordcount = 1

    for words in sentence3:
        if words == " ":
            sentence3_wordcount += 1
    return(sentence3_wordcount)


words1 = sentence_words1()
words2 = sentence_words2()
words3 = sentence_words3()

def longest_sentence(): 
    if words1 > words2 and words1 > words3:
        return(words1)
    elif words2 > words3:
        return(words2)
    else:
        return(words3)
    
print(longest_sentence())





