from tensorflow.python.eager.profiler_client import monitor


# Only in tensorflow==2.19.0
def test_case():
    monitor(None, -625, -625)
