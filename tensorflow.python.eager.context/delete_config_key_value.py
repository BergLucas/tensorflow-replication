from tensorflow.python.eager.context import Context


def test_case_0():
    context = Context(device_policy=None)
    context.delete_config_key_value("")
