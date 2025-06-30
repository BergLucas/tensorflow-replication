from tensorflow.python.framework.c_api_util import ApiDefMap


def test_case():
    api_def_map = ApiDefMap()
    api_def_map.get_api_def("")
