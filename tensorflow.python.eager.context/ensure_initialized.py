from tensorflow.python.eager.remote import connect_to_remote_host
from tensorflow.python.ops.math_ops import to_int64


# Only in tensorflow==2.19.0
def test_case():
    host = "bW5a ]"
    connect_to_remote_host(host)
    to_int64(host)
