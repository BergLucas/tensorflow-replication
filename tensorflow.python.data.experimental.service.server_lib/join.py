from tensorflow.python.data.experimental.service.server_lib import DispatchServer


def test_case():
    server = DispatchServer(start=None)
    server.join()
