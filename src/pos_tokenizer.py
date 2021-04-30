import nltk


def pos_tokenize(instr: str):
    nltk.download("punkt", quiet=True)
    nltk.download("averaged_perceptron_tagger", quiet=True)

    tokens = nltk.word_tokenize(instr)
    tagged = nltk.pos_tag(tokens)

    words = []
    pos = {}
    for x in tagged:
        if not x[0].lower() in words:
            words.append(x[0].lower())
        try:
            if not x[0].lower() in pos[x[1]]:
                pos[x[1]].append(x[0].lower())
        # FIXME: error here, exception needs to be specified
        except:
            ls = [x[0].lower()]
            pos[x[1]] = ls

    return pos, words


# Parts of speech IDs from nltk:
# CC coordinating conjunction
# CD cardinal digit
# DT determiner
# EX existential there
# FW foreign word
# IN preposition/subordinating conjunction
# JJ adjective 'big'
# JJR adjective, comparative 'bigger'
# JJS adjective, superlative 'biggest'
# LS list marker 1)
# MD modal could, will
# NN noun, singular 'desk'
# NNS noun plural 'desks'
# NNP proper noun, singular 'Harrison'
# NNPS proper noun, plural 'Americans'
# PDT predeterminer 'all the kids'
# POS possessive ending parent's
# PRP personal pronoun I, he, she
# PRP$ possessive pronoun my, his, hers
# RB adverb very, silently,
# RBR adverb, comparative better
# RBS adverb, superlative best
# RP particle give up
# TO to go 'to' the store.
# UH interjection errrrrrrrm
# VB verb, base form take
# VBD verb, past tense took
# VBG verb, gerund/present participle taking
# VBN verb, past participle taken
# VBP verb, sing. present, non-3d take
# VBZ verb, 3rd person sing. present takes
# WDT wh-determiner which
# WP wh-pronoun who, what
# WP$ possessive wh-pronoun whose
# WRB wh-abverb where, when
