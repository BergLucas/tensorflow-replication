from tensorflow.python.eager.tape import Tape


def test_case():
    tape = Tape("")
    tape.watched_variables()
