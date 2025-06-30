from tensorflow.python.eager.profiler_client import start_tracing


# Only in tensorflow==2.19.0
def test_case():
    start_tracing(None, None, True)
