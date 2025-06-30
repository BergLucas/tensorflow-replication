from tensorflow.python.eager.monitoring import SamplerCell


def test_case():
    sampler_cell = SamplerCell(None)
    sampler_cell.value()
