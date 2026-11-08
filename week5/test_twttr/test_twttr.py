from twttr import shorten


def test_lowercase():
    # pega código que não troca vogais minúsculas, ou que imprime em maiúsculo
    assert shorten("twitter") == "twttr"


def test_uppercase():
    # pega código que não remove vogais maiúsculas
    assert shorten("CALCULATOR") == "CLCLTR"


def test_mixed_case():
    assert shorten("Twitter") == "Twttr"


def test_numbers():
    # pega código que omite números
    assert shorten("CS50") == "CS50"
    assert shorten("R2D2") == "R2D2"


def test_punctuation():
    # pega código que omite pontuação
    assert shorten("What's your name?") == "Wht's yr nm?"


def test_empty():
    assert shorten("") == ""
