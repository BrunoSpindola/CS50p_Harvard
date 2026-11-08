from bank import value


def test_hello():
    # valores corretos para "hello"
    assert value("hello") == 0


def test_h_greeting():
    # valores corretos para saudações que começam com "h"
    assert value("hi") == 20
    assert value("how you doing?") == 20


def test_other():
    # valores corretos para o resto
    assert value("what's up?") == 100
    assert value("") == 100


def test_case_insensitive():
    # pega código que diferencia maiúsculas de minúsculas
    assert value("HELLO") == 0
    assert value("Hello") == 0
    assert value("HI") == 20
    assert value("How you doing?") == 20
    assert value("WHAT'S UP?") == 100


def test_entire_phrase():
    # pega código que só aceita "hello" exato
    assert value("hello, newman") == 0
    assert value("Hello, Newman") == 0
    assert value("hello there") == 0
