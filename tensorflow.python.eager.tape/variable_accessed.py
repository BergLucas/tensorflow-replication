from tensorflow.python.eager.tape import Tape, push_tape, variable_accessed


def test_case():
    tape = Tape([])
    push_tape(tape)
    variable_accessed(tape)
