from tensorflow.python.eager.monitoring import BoolGaugeCell


def test_case():
    bool_gauge_cell = BoolGaugeCell(None)
    bool_gauge_cell.set(None)
