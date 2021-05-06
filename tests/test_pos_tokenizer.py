import src.pos_tokenizer as tokenizer
import pytest

def test_tokenizer():
    pos, words = tokenizer.pos_tokenize("hello world, hows it going?")
    assert not len(words) == 0
    assert not len(pos) == 0
    assert words == ["hello", "world", ",", "hows", "it", "going" , "?"]

@pytest.mark.parametrize("word, expected",[("cars",True),("key",False),("trees",True),("houses",True)])
def test_is_plural(word, expected):
    is_plural, lemma = tokenizer.is_plural(word)
    assert is_plural == expected