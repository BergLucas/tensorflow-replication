from tensorflow.python.framework.kernels import get_registered_kernels_for_op


def test_case():
    get_registered_kernels_for_op(None)
