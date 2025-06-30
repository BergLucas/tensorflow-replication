from tensorflow.python.eager.record import VariableWatcher


def test_case():
    variable_watcher = VariableWatcher()
    variable_watcher.watched_variables()
