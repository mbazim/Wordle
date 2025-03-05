import pytest
from project import evaluate_guess, load_word_list, select_target_word

def test_evaluate_guess():
    assert evaluate_guess("HELLO", "HELLO") == ["correct", "correct", "correct", "correct", "correct"]

    assert evaluate_guess("ABCDE", "FGHIJ") == ["absent", "absent", "absent", "absent", "absent"]

    assert evaluate_guess("SOLAR", "SLICE") == ["correct", "absent", "absent", "absent", "absent"]

    assert evaluate_guess("RATES", "STARE") == ["present", "present", "present", "present", "present"]

    assert evaluate_guess("HELLO", "WORLD") == ["absent", "absent", "present", "correct", "absent"]
    
    assert evaluate_guess("GUESS", "SISSY") == ["absent", "absent", "correct", "present", "absent"]
    
    assert evaluate_guess("Apple", "APPLY") == ["correct", "correct", "correct", "correct", "absent"]

def test_load_word_list():
    word_list = load_word_list()
    assert isinstance(word_list, list)
    assert len(word_list) > 0
    
    for word in word_list:
        assert len(word) == 5
    
    for word in word_list:
        assert word.isupper()

def test_select_target_word():
    test_words = ["APPLE", "BEACH", "CLOUD", "DANCE", "EARTH"]
    
    selected_word = select_target_word(test_words)
    assert selected_word in test_words

    assert selected_word.isupper()
    
    selections = [select_target_word(test_words) for _ in range(20)]
    assert len(set(selections)) > 1, "The word selection doesn't appear to be random"