from tensorflow.python.eager.context import check_alive
from tensorflow.python.data.experimental.ops.random_ops import RandomDatasetV2


def test_case():
    RandomDatasetV2(rerandomize_each_iteration="")
    check_alive("")
