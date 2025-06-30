from tensorflow.python.eager.executor import Executor


def test_case():
    executor = Executor(None)
    executor.is_async()
