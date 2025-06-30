from tensorflow.python.eager.context import add_c_function


def test_case():
    add_c_function(None)
